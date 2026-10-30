extends Node3D

const TILE_SIZE := 2.0
const GRID_WIDTH := 13
const GRID_DEPTH := 18
const LANE_X := [2, 6, 10]

var terrain_root: Node3D
var actors_root: Node3D

func _ready() -> void:
    _build_scene()
    _build_board()
    _spawn_sample_units()
    _spawn_objectives()
    print("3D tactical prototype started")

func _build_scene() -> void:
    terrain_root = Node3D.new()
    terrain_root.name = "TerrainRoot"
    add_child(terrain_root)

    actors_root = Node3D.new()
    actors_root.name = "ActorsRoot"
    add_child(actors_root)

    var camera := Camera3D.new()
    camera.name = "MainCamera"
    camera.position = Vector3(0.0, 12.0, 18.0)
    camera.rotation_degrees = Vector3(-32.0, 0.0, 0.0)
    camera.current = true
    add_child(camera)

    var light := DirectionalLight3D.new()
    light.rotation_degrees = Vector3(-45.0, 35.0, 0.0)
    light.light_energy = 1.35
    add_child(light)

    var environment := WorldEnvironment.new()
    var env := Environment.new()
    env.background_mode = Environment.BG_COLOR
    env.background_color = Color(0.08, 0.11, 0.18)
    env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
    env.ambient_light_color = Color(0.8, 0.85, 1.0)
    env.ambient_light_energy = 0.9
    environment.environment = env
    add_child(environment)

func _build_board() -> void:
    for z in range(GRID_DEPTH):
        for x in range(GRID_WIDTH):
            var lane_index = _lane_index_for_x(x)
            var tile_data = _tile_data_for(x, z, lane_index)
            var tile := _create_tile(tile_data["position"], tile_data["color"], tile_data["height"])
            terrain_root.add_child(tile)

func _lane_index_for_x(x: int) -> int:
    var best_index := 0
    var best_distance := 1000
    for i in range(LANE_X.size()):
        var distance = abs(x - LANE_X[i])
        if distance < best_distance:
            best_distance = distance
            best_index = i
    return best_index

func _tile_data_for(x: int, z: int, lane_index: int) -> Dictionary:
    var lane_x = LANE_X[lane_index]
    var is_lane = abs(x - lane_x) <= 1
    var height := 0.0
    var color := Color(0.10, 0.22, 0.18)

    if z < 3:
        color = Color(0.18, 0.24, 0.42)
    elif z > GRID_DEPTH - 4:
        color = Color(0.45, 0.18, 0.16)

    if is_lane:
        color = Color(0.26, 0.28, 0.34)
    elif abs(x - lane_x) <= 2:
        color = Color(0.18, 0.30, 0.22)

    if z in [4, 8, 12] and is_lane:
        height = 0.35
        color = Color(0.36, 0.32, 0.22)

    if z in [6, 9, 14] and not is_lane:
        height = 0.2
        color = Color(0.15, 0.30, 0.22)

    if z in [2, 15] and abs(x - lane_x) <= 1:
        color = Color(0.22, 0.38, 0.28)

    var world_x = (float(x) - float(GRID_WIDTH) / 2.0) * TILE_SIZE
    var world_z = (float(z) - float(GRID_DEPTH) / 2.0) * TILE_SIZE
    return {
        "position": Vector3(world_x, 0.0, world_z),
        "height": height,
        "color": color,
    }

func _create_tile(position: Vector3, color: Color, height: float) -> Node3D:
    var tile := Node3D.new()
    tile.position = position

    var body := StaticBody3D.new()
    body.position = Vector3(0.0, 0.0, 0.0)

    var collision := CollisionShape3D.new()
    var shape := BoxShape3D.new()
    shape.size = Vector3(TILE_SIZE * 0.95, 0.8 + height, TILE_SIZE * 0.95)
    collision.shape = shape
    body.add_child(collision)

    var mesh := MeshInstance3D.new()
    var cube := BoxMesh.new()
    cube.size = Vector3(TILE_SIZE * 0.95, 0.8 + height, TILE_SIZE * 0.95)
    mesh.mesh = cube

    var material := StandardMaterial3D.new()
    material.albedo_color = color
    material.roughness = 0.88
    material.metallic = 0.08
    mesh.material_override = material
    mesh.position = Vector3(0.0, 0.0, 0.0)

    body.add_child(mesh)
    tile.add_child(body)
    return tile

func _spawn_sample_units() -> void:
    var team_a_colors := [Color(0.45, 0.74, 1.0), Color(0.75, 0.85, 1.0), Color(0.9, 0.7, 0.3)]
    var team_b_colors := [Color(1.0, 0.35, 0.35), Color(1.0, 0.7, 0.35), Color(0.7, 0.4, 1.0)]

    for lane_index in range(LANE_X.size()):
        var x = LANE_X[lane_index]
        var world_x = (float(x) - float(GRID_WIDTH) / 2.0) * TILE_SIZE
        var world_z_a = ((-GRID_DEPTH / 2.0) + 4.0) * TILE_SIZE
        var world_z_b = ((GRID_DEPTH / 2.0) - 4.0) * TILE_SIZE

        var unit_a := _create_unit(team_a_colors[lane_index], Vector3(world_x, 1.2, world_z_a))
        var unit_b := _create_unit(team_b_colors[lane_index], Vector3(world_x, 1.2, world_z_b))
        actors_root.add_child(unit_a)
        actors_root.add_child(unit_b)

func _create_unit(color: Color, position: Vector3) -> Node3D:
    var unit := CharacterBody3D.new()
    unit.position = position

    var body_mesh := MeshInstance3D.new()
    var capsule := CapsuleMesh.new()
    capsule.height = 1.2
    capsule.radius = 0.45
    body_mesh.mesh = capsule

    var material := StandardMaterial3D.new()
    material.albedo_color = color
    material.roughness = 0.5
    body_mesh.material_override = material

    unit.add_child(body_mesh)
    return unit

func _spawn_objectives() -> void:
    for lane_index in range(LANE_X.size()):
        var x = LANE_X[lane_index]
        var lane_world_x = (float(x) - float(GRID_WIDTH) / 2.0) * TILE_SIZE
        var z_front = ((GRID_DEPTH / 2.0) - 2.0) * TILE_SIZE
        var z_back = ((-GRID_DEPTH / 2.0) + 2.0) * TILE_SIZE

        var tower_a := _create_objective(Color(0.32, 0.62, 0.95), Vector3(lane_world_x, 2.0, z_back))
        var tower_b := _create_objective(Color(0.95, 0.36, 0.42), Vector3(lane_world_x, 2.0, z_front))
        actors_root.add_child(tower_a)
        actors_root.add_child(tower_b)

func _create_objective(color: Color, position: Vector3) -> Node3D:
    var objective := Node3D.new()
    objective.position = position

    var core := MeshInstance3D.new()
    var cylinder := CylinderMesh.new()
    cylinder.top_radius = 0.5
    cylinder.bottom_radius = 0.5
    cylinder.height = 3.2
    core.mesh = cylinder

    var material := StandardMaterial3D.new()
    material.albedo_color = color
    material.emission_enabled = true
    material.emission = color
    material.emission_energy_multiplier = 0.3
    core.material_override = material

    objective.add_child(core)
    return objective
