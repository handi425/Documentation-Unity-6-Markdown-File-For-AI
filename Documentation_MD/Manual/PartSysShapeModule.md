[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysShapeModule.html)
  * [中文](/cn/current/Manual/PartSysShapeModule.html)
  * [日本語](/ja/current/Manual/PartSysShapeModule.html)
  * [한국어](/kr/current/Manual/PartSysShapeModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysShapeModule.html)
  * [中文](/cn/current/Manual/PartSysShapeModule.html)
  * [日本語](/ja/current/Manual/PartSysShapeModule.html)
  * [한국어](/kr/current/Manual/PartSysShapeModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Shape module reference

[](PartSysEmissionModule.html)

Emission module reference

[](PartSysVelOverLifeModule.html)

Velocity over Lifetime module reference

# Shape module reference

Explore the Shape module properties to define the volume or surface from which
[particles](class-ParticleSystem.html)A small, simple image or mesh that is
emitted by a particle system. A particle system can display and move particles
in great numbers to represent a fluid or amorphous entity. The effect of all
the particles together creates the impression of the complete entity, such as
smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) can be emitted, and the direction of
the start velocity.

## Shapes in the Shape module

This section details the properties for each **Shape**.

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

### Sphere, Hemisphere

![The shape module when set to Sphere mode](../uploads/Main/ShapeModule.png)
The shape module when set to Sphere mode

**Note** : Sphere and Hemisphere have the same properties.

**Property** | **Function**  
---|---  
**Shape** | The shape of the emission volume.  
**Sphere** | Uniform particle emission in all directions.  
**Hemisphere** | Uniform particle emission in all directions on one side of a plane.  
**Radius** | The radius of the circular aspect of the shape.  
**Radius Thickness** | The proportion of the volume that emits particles. A value of 0 emits particles from the outer surface of the shape. A value of 1 emits particles from the entire volume. Values in between will use a proportion of the volume.  
**Texture** An image used when rendering a GameObject, Sprite, or UI element.
Textures are often applied to the surface of a mesh to give it visual detail.
[More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) | A texture to use for tinting and discarding particles.  
**Clip Channel** | A channel from the texture to use for discarding particles.  
**Clip Threshold** | When mapping particles to positions on the texture, discard any whose **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) color falls below this threshold.  
**Color affects Particles** | Multiply particle colors by the texture color.  
**Alpha affects Particles** | Multiply particle alphas by the texture alpha.  
**Bilinear Filtering** | When reading the texture, combine 4 neighboring samples for smoother changes in particle color, regardless of the texture dimensions.  
**Position** | Apply an offset to the emitter shape used for spawning particles.  
**Rotation** | Rotate the emitter shape used for spawning particles.  
**Scale** | Change the size of the emitter shape used for spawning particles.  
**Align to Direction** | Orient particles based on their initial direction of travel. This can be useful if you want to simulate, for example, chunks of car paint flying off a car’s bodywork during a **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision). If the orientation is not
satisfactory, you can also override it by applying a **Start Rotation** value
in the **Main** module.  
**Randomize Direction** | Blend particle directions towards a random direction. When set to 0, this setting has no effect. When set to 1, the particle direction is completely random.  
**Spherize Direction** | Blend particle directions towards a spherical direction, where they travel outwards from the center of their [Transform](http://mdeditor.infra.hq.unity3d.com/#class-Transform). When set to 0, this setting has no effect. When set to 1, the particle direction points outwards from the center (behaving identically to when the Shape is set to Sphere).  
**Randomize Position** | Move particles by a random amount, up to the specified value. When this is set to 0, this setting has no effect. Any other value will apply some randomness to the spawning positions of the particles.  
  
### Cone

![The shape module when set to Cone mode](../uploads/Main/ShapeModule1.png) The shape module when set to Cone mode **Property** | **Function**  
---|---  
**Shape** | The shape of the emission volume.  
**Cone** | Emit particles from the base or body of a cone. The particles diverge in proportion to their distance from the cone’s center line.  
**Angle** | The angle of the cone at its point. An angle of 0 produces a cylinder while an angle of 90 gives a flat disc.  
**Radius** | The radius of the circular aspect of the shape.  
**Radius Thickness** | The proportion of the volume that emits particles.A value of 0 emits particles from the outer surface of the shape. A value of 1 emits particles from the entire volume. Values in between will use a proportion of the volume.  
**Arc** | The angular portion of a full circle that forms the emitter’s shape.  
**Mode** | Define how Unity generates particles around the arc of the shape. When set to **Random** , Unity generates particles randomly around the arc. If using **Loop** , Unity generates particles sequentially around the arc of the shape, and loops back to the start at the end of each cycle. **Ping-Pong** is the same as **Loop** , except each consecutive loop happens in the opposite direction to the last. Finally, **Burst Spread** mode distributes particle generation evenly around the shape. This can give you an even spread of particles, compared to the default randomized behavior, where particles may clump together unevenly. **Burst Spread** is best used with burst emissions.  
**Spread** | The discrete intervals around the arc where particles may be generated. For example, a value of 0 allows particles to spawn anywhere around the arc, and a value of 0.1 only spawns particles at 10% intervals around the shape.  
**Speed** | The speed the emission position moves around the arc. Using the small black drop-down menu next to the value field, set this to **Constant** for the value to always remain the same, or **Curve** for the value to change over time. This option is only available if **Mode** is set to something other than **Random**  
**Length** | The length of the cone. This only applies when the **Emit from:** property is set to **Volume**.  
**Emit from:** | The part of the cone to emit particles from: **Base** or **Volume**.  
**Texture** | A texture to be used for tinting and discarding particles.  
**Clip Channel** | A channel from the texture to be used for discarding particles.  
**Clip Threshold** | When mapping particles to positions on the texture, discard any whose pixel color falls below this threshold.  
**Color affects Particles** | Multiply particle colors by the texture color.  
**Alpha affects Particles** | Multiply particle alphas by the texture alpha.  
**Bilinear Filtering** | When reading the texture, combine 4 neighboring samples for smoother changes in particle color, regardless of the texture dimensions.  
**Position** | Apply an offset to the emitter shape used for spawning particles.  
**Rotation** | Rotate the emitter shape used for spawning particles.  
**Scale** | Change the size of the emitter shape used for spawning particles.  
**Align to Direction** | Orient particles based on their initial direction of travel. This can be useful if you want to simulate, for example, chunks of car paint flying off a car’s bodywork during a collision. If the orientation is not satisfactory, you can also override it by applying a Start Rotation value in the Main module.  
**Randomize Direction** | Blend particle directions towards a random direction. When set to 0, this setting has no effect. When set to 1, the particle direction is completely random.  
**Spherize Direction** | Blend particle directions towards a spherical direction, where they travel outwards from the center of their Transform. When set to 0, this setting has no effect. When set to 1, the particle direction points outwards from the center (behaving identically to when the Shape is set to Sphere).  
**Randomize Position** | Move particles by a random amount, up to the specified value. When this is set to 0, this setting has no effect. Any other value will apply some randomness to the spawning positions of the particles. The amount of randomization is multiplied by the Scale property.  
  
### Box

![The shape module when set to Box mode](../uploads/Main/ShapeModule2.png) The shape module when set to Box mode **Property** | **Function**  
---|---  
**Shape** | The shape of the emission volume.  
**Box** | Emit particles from the edge, surface, or body of a box shape. The particles move in the emitter object’s forward (Z) direction.  
**Emit from:** | Select the part of the box to emit from: **Edge** , **Shell** , or **Volume**.  
**Texture** | A texture to be used for tinting and discarding particles.  
**Clip Channel** | A channel from the texture to be used for discarding particles.  
**Clip Threshold** | When mapping particles to positions on the texture, discard any whose pixel color falls below this threshold.  
**Color affects Particles** | Multiply particle colors by the texture color.  
**Alpha affects Particles** | Multiply particle alphas by the texture alpha.  
**Bilinear Filtering** | When reading the texture, combine 4 neighboring samples for smoother changes in particle color, regardless of the texture dimensions.  
**Position** | Apply an offset to the emitter shape used for spawning particles.  
**Rotation** | Rotate the emitter shape used for spawning particles.  
**Scale** | Change the size of the emitter shape used for spawning particles.  
**Align to Direction** | Orient particles based on their initial direction of travel. This can be useful if you want to simulate, for example, chunks of car paint flying off a car’s bodywork during a collision. If the orientation is not satisfactory, you can also override it by applying a Start Rotation value in the Main module.  
**Randomize Direction** | Blend particle directions towards a random direction. When set to 0, this setting has no effect. When set to 1, the particle direction is completely random.  
**Spherize Direction** | Blend particle directions towards a spherical direction, where they travel outwards from the center of their Transform. When set to 0, this setting has no effect. When set to 1, the particle direction points outwards from the center (behaving identically to when the Shape is set to Sphere).  
**Randomize Position** | Move particles by a random amount, up to the specified value. When this is set to 0, this setting has no effect. Any other value will apply some randomness to the spawning positions of the particles.  
  
### Mesh, MeshRenderer, SkinnedMeshRenderer

![The shape module when set to Mesh mode](../uploads/Main/ShapeModule3.png)
The shape module when set to Mesh mode

Mesh, MeshRenderer and SkinnedMeshRenderer have the same properties.

**Property** | **Function**  
---|---  
**Shape** | The shape of the emission volume.  
**Mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) | Emits particles from any arbitrary Mesh shape supplied via the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).  
**MeshRenderer** | Emits particles from a reference to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)’s **Mesh Renderer** A mesh
component that takes the geometry from the Mesh Filter and renders it at the
position defined by the object’s Transform component. [More info](class-
MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer).  
**SkinnedMeshRenderer** | Emits particles from a reference to a GameObject’s Skinned Mesh Renderer.  
**Type** | Where particles are emitted from. Select **Vertex** for the particles to emit from the vertices, **Edge** for the particles to emit from the edges, or **Triangle** for the particles to emit from the triangles. This is set to **Vertex** by default.  
**Mode** | How the position on the mesh is chosen for each new particle. Select **Random** for the particles to choose a random position **Loop** for each new particle to be emitted from the next vertex in the mesh, or **Ping-Pong** to behave similarly to Loop mode, but to alternate the direction along the mesh vertices after each cycle. This is set to **Random** by default.  
**Mesh** | The Mesh that provides the emitter’s shape.  
**Single Material** | Specify whether to emit particles from a particular sub-Mesh (identified by the material index number). If enabled, a numeric field appears, which allows you to specify the material index number.  
**Use Mesh Colors** | Modulate particle color with Mesh vertex colors, or, if they don’t exist, use the **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) color property “ _Color“ or ”_
TintColor” from the material.  
**Normal Offset** | Distance away from the surface of the Mesh to emit particles (in the direction of the surface normal)  
**Texture** | A texture to be used for tinting and discarding particles.  
**Clip Channel** | A channel from the texture to be used for discarding particles.  
**Clip Threshold** | When mapping particles to positions on the texture, discard any whose pixel color falls below this threshold.  
**Color Affects Particles** | Multiply particle colors by the texture color.  
**Alpha Affects Particles** | Multiply particle alphas by the texture alpha.  
**Bilinear Filtering** | When reading the texture, combine 4 neighboring samples for smoother changes in particle color, regardless of the texture dimensions.  
**UV Channel** | Choose which UV channel on the source mesh to use for sampling the texture.  
**Position** | Apply an offset to the emitter shape used for spawning particles.  
**Rotation** | Rotate the emitter shape used for spawning particles.  
**Scale** | Change the size of the emitter shape used for spawning particles.  
**Align to Direction** | Orient particles based on their initial direction of travel. This can be useful if you want to simulate, for example, chunks of car paint flying off a car’s bodywork during a collision. If the orientation is not satisfactory, you can also override it by applying a Start Rotation value in the Main module.  
**Randomize Direction** | Blend particle directions towards a random direction. When set to 0, this setting has no effect. When set to 1, the particle direction is completely random.  
**Spherize Direction** | Blend particle directions towards a spherical direction, where they travel outwards from the center of their Transform. When set to 0, this setting has no effect. When set to 1, the particle direction points outwards from the center (behaving identically to when the Shape is set to Sphere).  
**Randomize Position** | Move particles by a random amount, up to the specified value. When this is set to 0, this setting has no effect. Any other value will apply some randomness to the spawning positions of the particles.  
  
### Sprite and Sprite Renderer

![The shape module when set to Sprite
mode](../uploads/Main/ShapeModuleSprite.png) The shape module when set to
Sprite mode

Sprite and SpriteRenderer have the same properties.

**Property** | **Function**  
---|---  
**Shape** | The shape of the emission volume.  
**Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are
essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) | Emits particles from a Sprite shape supplied via the Inspector.  
**SpriteRenderer** | Emits particles from a reference to a GameObject’s **Sprite Renderer** A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](sprite/renderer/renderer-landing.html)  
See in [Glossary](Glossary.html#SpriteRenderer).  
**Type** | Where particles are emitted from. Select **Vertex** to emit particles from the vertices, **Edge** to emit particles from the edges, or **Triangle** to emit particles from the triangles. This is set to **Vertex** by default.  
**Sprite** | The Sprite that defines the particle emitter’s shape.  
**Normal Offset** | Distance away from the surface of the Sprite to emit particles (in the direction of the surface normal)  
**Texture** | A texture to be used for tinting and discarding particles.  
**Clip Channel** | A channel from the texture to be used for discarding particles.  
**Clip Threshold** | When mapping particles to positions on the texture, discard any whose pixel color falls below this threshold.  
**Color Affects Particles** | Multiply particle colors by the texture color.  
**Alpha Affects Particles** | Multiply particle alphas by the texture alpha.  
**Bilinear Filtering** | When reading the texture, combine 4 neighboring samples for smoother changes in particle color, regardless of the texture dimensions.  
**Position** | Apply an offset to the emitter shape used for spawning particles.  
**Rotation** | Rotate the emitter shape used for spawning particles.  
**Scale** | Change the size of the emitter shape used for spawning particles.  
**Align to Direction** | Orient particles based on their initial direction of travel. This can be useful if you want to simulate, for example, chunks of car paint flying off a car’s bodywork during a collision. If the orientation is not satisfactory, you can also override it by applying a Start Rotation value in the Main module.  
**Randomize Direction** | Blend particle directions towards a random direction. When set to 0, this setting has no effect. When set to 1, the particle direction is completely random.  
**Spherize Direction** | Blend particle directions towards a spherical direction, where they travel outwards from the center of their Transform. When set to 0, this setting has no effect. When set to 1, the particle direction points outwards from the center (behaving identically to when the Shape is set to Sphere).  
**Randomize Position** | Move particles by a random amount, up to the specified value. When this is set to 0, this setting has no effect. Any other value will apply some randomness to the spawning positions of the particles.  
  
### Circle

![The shape module when set to Circle mode](../uploads/Main/ShapeModule4.png) The shape module when set to Circle mode **Property** | **Function**  
---|---  
**Shape** | The shape of the emission volume.  
**Circle** | Uniform particle emission from the center or edge of a circle. The particles move only in the plane of the circle.  
**Radius** | The radius of the circular aspect of the shape.  
**Radius Thickness** | The proportion of the volume that emits particles. A value of 0 emits particles from the outer edge of the circle. A value of 1 emits particles from the entire area. Values in between will use a proportion of the area.  
**Arc** | The angular portion of a full circle that forms the emitter’s shape.  
**Mode** | Define how Unity generates particles around the arc of the shape. When set to **Random** , Unity generates particles randomly around the arc. If using **Loop** , Unity generates particles sequentially around the arc of the shape, and loops back to the start at the end of each cycle. **Ping-Pong** is the same as **Loop** , except each consecutive loop happens in the opposite direction to the last. Finally, **Burst Spread** mode distributes particle generation evenly around the shape. This can be used to give you an even spread of particles, compared to the default randomized behavior, where particles may clump together unevenly. Burst Spread is best used with burst emissions.  
**Spread** | Control the discrete intervals around the arc where particles may be generated. For example, a value of 0 will allow particles to spawn anywhere around the arc, and a value of 0.1 will only spawn particles at 10% intervals around the shape.  
**Speed** | Set a value for the speed the emission position moves around the arc. Using the small black drop-down next to the value field, set this to **Constant** for the value to always remain the same, or **Curve** for the value to change over time.  
**Texture** | Choose a texture to be used for tinting and discarding particles.  
**Clip Channel** | Select a channel from the texture to be used for discarding particles.  
**Clip Threshold** | When mapping particles to positions on the texture, discard any whose pixel color falls below this threshold.  
**Color Affects Particles** | Multiply particle colors by the texture color.  
**Alpha Affects Particles** | Multiply particle alphas by the texture alpha.  
**Bilinear Filtering** | When reading the texture, combine 4 neighboring samples, for smoother changes in particle color, regardless of the texture dimensions.  
**Position** | Apply an offset to the emitter shape used for spawning particles.  
**Rotation** | Rotate the emitter shape used for spawning particles.  
**Scale** | Change the size of the emitter shape used for spawning particles.  
**Align to Direction** | Use this checkbox to orient particles based on their initial direction of travel. This can be useful if you want to simulate, for example, chunks of car paint flying off a car’s bodywork during a collision. If the orientation is not satisfactory, you can also override it by applying a Start Rotation value in the Main module.  
**Randomize Direction** | Blend particle directions towards a random direction. When set to 0, this setting has no effect. When set to 1, the particle direction is completely random.  
**Spherize Direction** | Blend particle directions towards a spherical direction, where they travel outwards from the center of their Transform. When set to 0, this setting has no effect. When set to 1, the particle direction points outwards from the center (behaving identically to when the Shape is set to Sphere).  
**Randomize Position** | Move particles by a random amount, up to the specified value. When this is set to 0, this setting has no effect. Any other value will apply some randomness to the spawning positions of the particles.  
  
### Edge

![The shape module when set to Edge mode](../uploads/Main/ShapeModule5.png) The shape module when set to Edge mode **Property** | **Function**  
---|---  
**Shape** | The shape of the emission volume.  
**Edge** | Emit particles from a line segment. The particles move in the emitter object’s upward (Y) direction.  
**Radius** | The radius property is used to define the length of the edge.  
**Mode** | Define how Unity generates particles along the radius of the shape. When set to **Random** , Unity generates particles randomly along the radius. If using **Loop** , Unity generates particles sequentially along the radius of the shape, and loops back to the start at the end of each cycle. **Ping-Pong** is the same as **Loop** , except each consecutive loop happens in the opposite direction to the last. Finally, **Burst Spread** mode distributes particle generation evenly along the radius. This can be used to give you an even spread of particles, compared to the default randomized behavior, where particles may clump together unevenly. Burst Spread is best used with burst emissions.  
**Spread** | T the discrete intervals along the radius where particles may be generated. For example, a value of 0 will allow particles to spawn anywhere along the radius, and a value of 0.1 will only spawn particles at 10% intervals along the radius.  
**Speed** | The speed the emission position moves along the radius. Using the small black drop-down next to the value field, set this to **Constant** for the value to always remain the same, or **Curve** for the value to change over time.  
**Texture** | A texture to be used for tinting and discarding particles.  
**Clip Channel** | A channel from the texture to be used for discarding particles.  
**Clip Threshold** | When mapping particles to positions on the texture, discard any whose pixel color falls below this threshold.  
**Color Affects Particles** | Multiply particle colors by the texture color.  
**Alpha Affects Particles** | Multiply particle alphas by the texture alpha.  
**Bilinear Filtering** | When reading the texture, combine 4 neighboring samples for smoother changes in particle color, regardless of the texture dimensions.  
**Position** | Apply an offset to the emitter shape used for spawning particles.  
**Rotation** | Rotate the emitter shape used for spawning particles.  
**Scale** | Change the size of the emitter shape used for spawning particles.  
**Align to Direction** | Orient particles based on their initial direction of travel. This can be useful if you want to simulate, for example, chunks of car paint flying off a car’s bodywork during a collision. If the orientation is not satisfactory, you can also override it by applying a **Start Rotation** value in the Main module.  
**Randomize Direction** | Blend particle directions towards a random direction. When set to 0, this setting has no effect. When set to 1, the particle direction is completely random.  
**Spherize Direction** | Blend particle directions towards a spherical direction, where they travel outwards from the center of their Transform. When set to 0, this setting has no effect. When set to 1, the particle direction points outwards from the center (behaving identically to when the Shape is set to Sphere).  
**Randomize Position** | Move particles by a random amount, up to the specified value. When this is set to 0, this setting has no effect. Any other value will apply some randomness to the spawning positions of the particles.  
  
### Donut

![The shape module when set to Donut mode](../uploads/Main/ShapeModule6.png) The shape module when set to Donut mode **Property** | Function  
---|---  
**Shape** | The shape of the emission volume.  
**Donut** | Emit particles from a torus. The particles move outwards from the ring of the Torus.  
**Radius** | The radius of the main donut ring.  
**Donus Radius** | The thickness of the outer donut ring.  
**Radius Thickness** | The proportion of the volume that emits particles. A value of 0 emits particles from the outer edge of the circle. A value of 1 emits particles from the entire area. Values in between will use a proportion of the area.  
**Arc** | The angular portion of a full circle that forms the emitter’s shape.  
Mode | Define how Unity generates particles around the arc of the shape. When set to **Random** , Unity generates particles randomly around the arc. If using **Loop** , Unity generates particles sequentially around the arc of the shape, and loops back to the start at the end of each cycle. **Ping-Pong** is the same as **Loop** , except each consecutive loop happens in the opposite direction to the last. Finally, **Burst Spread** mode distributes particle generation evenly around the shape. This can be used to give you an even spread of particles, compared to the default randomized behavior, where particles may clump together unevenly. Burst Spread is best used with burst emissions.  
Spread | The discrete intervals around the arc where particles may be generated. For example, a value of 0 will allow particles to spawn anywhere around the arc, and a value of 0.1 will only spawn particles at 10% intervals around the shape.  
Speed | The speed the emission position moves around the arc. Using the small black drop-down next to the value field, set this to **Constant** for the value to always remain the same, or **Curve** for the value to change over time.  
**Texture** | A texture to be used for tinting and discarding particles.  
**Clip Channel** | A channel from the texture to be used for discarding particles.  
**Clip Threshold** | When mapping particles to positions on the texture, discard any whose pixel color falls below this threshold.  
**Color Affects Particles** | Multiply particle colors by the texture color.  
**Alpha Affects Particles** | Multiply particle alphas by the texture alpha.  
**Bilinear Filtering** | When reading the texture, combine 4 neighboring samples for smoother changes in particle color, regardless of the texture dimensions.  
**Position** | Apply an offset to the emitter shape used for spawning particles.  
**Rotation** | Rotate the emitter shape used for spawning particles.  
**Scale** | Change the size of the emitter shape used for spawning particles.  
**Align To Direction** | Orient particles based on their initial direction of travel. This can be useful if you want to simulate, for example, chunks of car paint flying off a car’s bodywork during a collision. If the orientation is not satisfactory, you can also override it by applying a **Start Rotation** value in the Main module.  
**Randomize Direction** | Blend particle directions towards a random direction. When set to 0, this setting has no effect. When set to 1, the particle direction is completely random.  
**Spherize Direction** | Blend particle directions towards a spherical direction, where they travel outwards from the center of their Transform. When set to 0, this setting has no effect. When set to 1, the particle direction points outwards from the center (behaving identically to when the Shape is set to Sphere).  
**Randomize Position** | Move particles by a random amount, up to the specified value. When this is set to 0, this setting has no effect. Any other value will apply some randomness to the spawning positions of the particles.  
  
### Rectangle

![The shape module when set to Rectangle mode](../uploads/Main/ShapeModule7.png) The shape module when set to Rectangle mode **Property** | Function  
---|---  
**Shape** | The shape of the emission volume.  
**Rectangle** | Emits particles from a rectangle. The particles move up from the rectangle.  
**Texture** | A texture to be used for tinting and discarding particles.  
**Clip Channel** | A channel from the texture to be used for discarding particles.  
**Clip Threshold** | When mapping particles to positions on the texture, discard any whose pixel color falls below this threshold.  
**Color Affects Particles** | Multiply particle colors by the texture color.  
**Alpha Affects Particles** | Multiply particle alphas by the texture alpha.  
**Bilinear Filtering** | When reading the texture, combine 4 neighboring samples for smoother changes in particle color, regardless of the texture dimensions.  
**Position** | Apply an offset to the emitter shape used for spawning particles.  
**Rotation** | Rotate the emitter shape used for spawning particles.  
**Scale** | Change the size of the emitter shape used for spawning particles.  
**Align To Direction** | Orient particles based on their initial direction of travel. This can be useful if you want to simulate, for example, chunks of car paint flying off a car’s bodywork during a collision. If the orientation is not satisfactory, you can also override it by applying a **Start Rotation** value in the Main module.  
**Randomize Direction** | Blend particle directions towards a random direction. When set to 0, this setting has no effect. When set to 1, the particle direction is completely random.  
**Spherize Direction** | Blend particle directions towards a spherical direction, where they travel outwards from the center of their Transform. When set to 0, this setting has no effect. When set to 1, the particle direction points outwards from the center (behaving identically to when the Shape is set to Sphere).  
**Randomize Position** | Move particles by a random amount, up to the specified value. When this is set to 0, this setting has no effect. Any other value will apply some randomness to the spawning positions of the particles.  
  
## Additional resources

  * [Particle emissions and emitters](particle-emissions-emitters.html)

[](PartSysEmissionModule.html)

Emission module reference

[](PartSysVelOverLifeModule.html)

Velocity over Lifetime module reference

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

