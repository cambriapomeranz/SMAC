# Install Ursina before using this "pip install ursina"
# Tutorial https://www.youtube.com/watch?v=DHSRaVeQxIk
# What are you doing here?!

# Imports
from turtle import position, pu
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random 
import numpy as np
from search import search
from path_conversion import * 
from config import BD_LOC
import time
import copy 

app = Ursina()

# Variables
grass_texture = load_texture("Assets/Textures/white_block.png")
stone_texture = load_texture("Assets/Textures/Stone_Block.png")
brick_texture = load_texture("Assets/Textures/Brick_Block.png")
dirt_texture = load_texture("Assets/Textures/Dirt_Block.png")
wood_texture = load_texture("Assets/Textures/Wood_Block.png")
sky_texture = load_texture("Assets/Textures/Skybox.png")
arm_texture = load_texture("Assets/Textures/Arm_Texture.png")
smart_block_texture = load_texture("Assets/Textures/smart_block.png")
smart_block_texture_step = load_texture("Assets/Textures/smart_block_step.png")
smart_block_texture_red = load_texture("Assets/Textures/smart_block_red_outline.png")
smart_block_texture_blue = load_texture("Assets/Textures/smart_block_blue_outline.png")
smart_block_texture_yellow = load_texture("Assets/Textures/smart_block_yellow_outline.png")
smart_block_texture_green = load_texture("Assets/Textures/smart_block_neon_green_outline.png")
smart_block_outline = load_texture("Assets/Textures/smart_block_outline.png")
arrow_block = load_texture("Assets/Textures/arrow_block.png")

#Color Steps
smart_block_texture_step_red = load_texture("Assets/Textures/smart_block_red_step.png")
smart_block_texture_step_blue = load_texture("Assets/Textures/smart_block_blue_step.png")
smart_block_texture_step_yellow = load_texture("Assets/Textures/smart_block_yellow_step.png")
smart_block_texture_step_green = load_texture("Assets/Textures/smart_block_green_step.png") 

color_index_1 = smart_block_texture_red
color_index_2 = smart_block_texture_blue
color_index_3 = smart_block_texture_yellow
color_index_4 = smart_block_texture_green
last_colored_block = None
last_block_original_texture = None
last_colored_block_2 = None
last_block_original_texture_2 = None

window.exit_button.visible = False
block_pick = 1
index = 0
key_9_pressed = False  
key_6_pressed = False  
key_n_pressed = False 
key_p_pressed = False
placed_block = None 
spawned = False
spawn_x, spawn_y, spawn_z = 0, 0, 0

blocks_placed = []
found_structures = []
coords_to_spawn = []
misc_blocks = []
complete_steps = []
path_steps = None 


number = 0 

point = [1, 0, 1]
prev_point = [1, 0, 1]

# Updates every frame
def update():
    global blocks_placed, block_pick, key_9_pressed, key_6_pressed, key_p_pressed, key_n_pressed, coords_to_spawn, last_colored_block, last_block_original_texture, last_colored_block_2, last_block_original_texture_2, found_structures, misc_blocks, prev_point, point, placed_block, spawned, spawn_x, spawn_y, spawn_z, goal, number , path_steps

    if held_keys["1"]: block_pick = 1
    if held_keys["2"]: block_pick = 2
    if held_keys["3"]: block_pick = 3
    if held_keys["4"]: block_pick = 4
    if held_keys["5"]: block_pick = 5

    # Generate the pyramid coordinates
    if held_keys["6"] and not key_6_pressed:
        pyramid_coordinates = generate_pyramid(5)
        # Spawn cubes for each coordinate in the pyramid
        for x, y, z in pyramid_coordinates:
            spawn_cube(x, y, z,'')  # Replace
            cube = Voxel(position=Vec3(x, y, z),  texture=smart_block_texture)
            blocks_placed.append(cube.position) 

        key_6_pressed = True  # Set the flag to True after printing
    
    if not held_keys["6"]:
        key_6_pressed = False
    
    if held_keys["7"]: 
        test_bfs()

    # Search(Look) for structures
    if held_keys["l"]:
        found_structures, misc_blocks = show_structures()

    if held_keys["p"] and not key_p_pressed:
        #delete_cube(BD_LOC[0], BD_LOC[1], BD_LOC[2])
        spawn_cube(BD_LOC[0], BD_LOC[1], BD_LOC[2], 'n')
       # test_structure =  [((10, 1, 12), (10, 1, 11), (10, 1, 10), (10, 2, 10), (10, 2, 11),(10, 3, 10))]
        print("leftover blocks: ", misc_blocks)
        coords_to_spawn, path_steps , goal= dev_total_path_steps(found_structures, misc_blocks)
        step_getter(path_steps)
        print("coords_to_spawn:")
        print(coords_to_spawn)

        for point in goal:
            point[1] += 1  # Increment the second value

        key_p_pressed = True

    if not held_keys["p"] and key_p_pressed:
        key_p_pressed = False

    if held_keys["n"] and not key_n_pressed and coords_to_spawn:
        (point, holding_block) = coords_to_spawn.pop(0)  # Get the next point
        x, z, y = point
        if holding_block:
            z = z+1

        already_placed_block = None
        for e in scene.entities:
            if hasattr(e, 'position') and e.position == Vec3(x, z, y):
                already_placed_block = e
                break

        print("spawned_block?", spawned)
        # first check if the last_colored_block was spawned bc we need to delete that block from blocks_placed and despawn it
        if spawned:
            print("trying to delete block")
            print("x: ", spawn_x)
            print("y: ", spawn_y)
            print("z: ", spawn_z)
            delete_cube(spawn_x, spawn_z, spawn_y)
            spawned = False

        # If there is a previously colored block, restore to original texture

        elif last_colored_block is not None:
            # if (last_colored_block.position.x, last_colored_block.position.y, last_colored_block.position.z) in blocks_placed:
            #     last_colored_block.texture = smart_block_texture  # Set to black if it's in blocks_placed
            # else:
                last_colored_block.texture = last_block_original_texture
        if already_placed_block:


            # Store the original texture before changing it
            last_block_original_texture = already_placed_block.texture
            print('goal in main is:', tuple(map(float, goal[number])))
            print((already_placed_block.position.x , already_placed_block.position.y , already_placed_block.position.z))
            if (already_placed_block.position.x, already_placed_block.position.y, already_placed_block.position.z) == tuple(map(float, goal[number])):
            # if (already_placed_block.position.x , already_placed_block.position.y , already_placed_block.position.z) in blocks_placed and last_block_original_texture in [smart_block_texture_step_blue, smart_block_texture_step_red, smart_block_texture_step_yellow, smart_block_texture_step_green]:
                print('goal reached')
                last_block_original_texture = smart_block_texture
                new_texture = smart_block_texture 
                number += 1
            else:
                new_texture = check_block_color(already_placed_block.position.x, already_placed_block.position.y, already_placed_block.position.z)
                print('new_texture:',new_texture)
            already_placed_block.texture = new_texture
            last_colored_block = already_placed_block

        else:
            print("spawning smart block cube")
            spawned = True
            spawned_block = spawn_cube(x, z, y,'step')
            spawn_x, spawn_y, spawn_z = x, y, z
            print("x: ", spawn_x)
            print("y: ", spawn_y)
            print("z: ", spawn_z)
            last_colored_block = spawned_block
            last_block_original_texture = smart_block_texture

        key_n_pressed = True

    if not held_keys["n"] and key_n_pressed:
        x2, z2, y2 = prev_point
        already_placed_block_2 = None
        for e in scene.entities:
            if hasattr(e, 'position') and e.position == Vec3(x2, z2, y2):
                already_placed_block_2 = e
                break

        # If there is a previously colored block, restore to original texture
        if last_colored_block_2 is not None:
            # if (last_colored_block_2.position.x, last_colored_block_2.position.z, last_colored_block_2.position.y) in blocks_placed:
            #     last_colored_block_2.texture = smart_block_texture  # Set to black if it's in blocks_placed
            # else:
            last_colored_block_2.texture = last_block_original_texture_2
        
        if already_placed_block_2:
            # Store the original texture before changing it
            last_block_original_texture_2 = already_placed_block_2.texture
            new_texture2 = check_block_color(already_placed_block_2.position.x, already_placed_block_2.position.y, already_placed_block_2.position.z)
            already_placed_block_2.texture = new_texture2
            last_colored_block_2 = already_placed_block_2
        else:
            spawned_block_2 = spawn_cube(x2, z2, y2,'step')
            last_colored_block_2 = spawned_block_2
            last_block_original_texture_2 = smart_block_texture

        prev_point = point
        key_n_pressed = False
                    
    if held_keys["9"] and not key_9_pressed:
        print(blocks_placed)
        key_9_pressed = True  # Set the flag to True after printing
    # Reset the flag when '9' is no longer held down
    if not held_keys["9"]:
        key_9_pressed = False


def step_getter(steps):
    complete_steps = copy.deepcopy(steps)
    file_path = "steps.txt"
    
    with open(file_path, 'w') as file:
        for step in complete_steps:
            file.write(f"{step}\n")
    

# Searches for known structures and changes the color of strucutres found 
def show_structures():
    found_structures, misc_blocks = search(blocks_placed)
    for structure in found_structures:
        structure_pos = structure[1]  
        structure_name = structure[0] #string
        for block in structure_pos:
            delete_cube(block[0], block[1], block[2])
            spawn_cube(block[0], block[1], block[2], structure_name[-1])
            print('structure_name:', structure_name[-1])
            #WHEN WE ARE IMPLEMENTING THE COLORS  spawn_cube(block[0], block[1], block[2], color_index)
        for block in misc_blocks:
            delete_cube(block[0], block[1], block[2])
            spawn_cube(block[0], block[1], block[2], 'misc')
        # else:
        #     delete_cube(block[0], block[1], block[2])
        #     spawn_cube(block[0], block[1], block[2], 'misc')
    return found_structures, misc_blocks

# Voxel (block) properties
class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = "Assets/Models/Block",
            origin_y = 0.5,
            texture = texture,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color = color.light_gray,
            scale = 0.5
        )

    # What happens to blocks on inputs
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position = self.position + mouse.normal, texture = smart_block_texture) 
                # only add blocks above field
                if(voxel.position[1] > 0):
                    blocks_placed.append(voxel.position) 
                    # print(new_voxel.position)
                print(blocks_placed)
            if key == "right mouse down":
                try: 
                    blocks_placed.remove(self.position)
                except Exception as e: 
                    print("Block not found")
                destroy(self)

# Skybox
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "Sphere",
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )

# Arm
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "Assets/Models/Arm",
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
        )
    
    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)

def generate_pyramid(base_size):
    pyramid = []
    # Each layer
    for y in range(base_size):
        # Each row
        for x in range(base_size - y):
            # Each column
            for z in range(base_size - y):
                pyramid.append((x+10, y+1, z+10))
    return pyramid

def check_block_color(x, y, z):
    block_color = None
    target_position = Vec3(x, y, z)
    existing_cube_texture = None
    for e in scene.entities:
        if hasattr(e, 'position') and e.position == target_position:
            if hasattr(e, 'texture'):  # Assuming entities have a 'texture' attribute
                existing_cube_texture = e.texture
                print(f"Found texture: {existing_cube_texture}")  
            break  # Stop searching once a block at the target position is found

    # If the position is occupied for stepping 
    if existing_cube_texture is not None:
        if existing_cube_texture == smart_block_texture: 
                block_color = smart_block_texture_step
        elif existing_cube_texture == grass_texture: 
                block_color = smart_block_texture_step_red
                print('here')
        elif existing_cube_texture == smart_block_texture_red: 
                block_color = smart_block_texture_step_red
        elif existing_cube_texture == smart_block_texture_green: 
                block_color = smart_block_texture_step_green
        elif existing_cube_texture == smart_block_texture_blue: 
                block_color = smart_block_texture_step_blue 
        elif existing_cube_texture == smart_block_texture_yellow: 
                block_color = smart_block_texture_step_yellow
        elif existing_cube_texture == smart_block_texture_step: 
                block_color = smart_block_texture_step
        elif existing_cube_texture == smart_block_texture_step_red:
                block_color = smart_block_texture_step_red
        elif existing_cube_texture == smart_block_texture_step_green:
                block_color = smart_block_texture_step_green
        elif existing_cube_texture == smart_block_texture_step_blue:
                block_color = smart_block_texture_step_blue
        elif existing_cube_texture == smart_block_texture_step_yellow:      
                block_color = smart_block_texture_step_yellow
        else:
                print(f"Unexpected texture: {existing_cube_texture}")  # Debugging line

    
    print('RETURNING block_color as:', block_color)
    return block_color


def spawn_cube(x, y, z, color_index):
    # First, check if the position is already occupied
    target_position = Vec3(x, y, z)

    # Assign color_index based on the input
    if color_index == 'n':
        color_index = color_index_1
    elif color_index == 's':
        color_index = color_index_2
    elif color_index == 'e':
        color_index = color_index_3
    elif color_index == 'w':
        color_index = color_index_4
    elif color_index == 'step':
        color_index = smart_block_texture_step
    elif color_index == 'misc':
        color_index = smart_block_outline    
    else:
        color_index = smart_block_texture

    # Spawn the cube
    new_cube = Voxel(position=target_position, texture=color_index)
    blocks_placed.append(target_position)  # Optionally update the blocks_placed list

def delete_cube(x, y, z):
    target_position = Vec3(x, y, z)
    for e in scene.entities:
        if hasattr(e, 'position') and e.position == target_position:
            destroy(e)
            if target_position in blocks_placed:
                blocks_placed.remove(target_position)
            break

# Increase the numbers for more cubes. For exapmle: for z in range(20)
for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x, 0, z))

player = FirstPersonController()
sky = Sky()

app.run()