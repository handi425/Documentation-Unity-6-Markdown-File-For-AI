[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tree-Root-Node.html)
  * [中文](/cn/current/Manual/tree-Root-Node.html)
  * [日本語](/ja/current/Manual/tree-Root-Node.html)
  * [한국어](/kr/current/Manual/tree-Root-Node.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tree-Root-Node.html)
  * [中文](/cn/current/Manual/tree-Root-Node.html)
  * [日本語](/ja/current/Manual/tree-Root-Node.html)
  * [한국어](/kr/current/Manual/tree-Root-Node.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](class-Tree.html)
  * Root node reference

[](terrain-Tree-Hierarchy-UI.html)

Tree Hierarchy view UI reference

[](tree-Branches.html)

Branch group reference

# Root node reference

The root node has properties that affect the entire tree, although you can
override some properties at the branch or leaf group level.

## Distribution

**Property** | **Function**  
---|---  
**Tree Seed** | The randomizing seed for the tree. Change the seed to vary the tree’s procedural generation. Note that the seed from the **root node** A transform in an animation hierarchy that allows Unity to establish consistency between Animation clips for a generic model. It also enables Unity to properly blend between Animations that have not been authored “in place” (that is, where the whole Model moves its world position while animating). [More info](AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](Glossary.html#Rootnode) changes the structure of the whole
tree, including all branch groups, whereas seeds from a branch group change
only that group.  
**Area Spread** | The tree’s radius. This parameter has an effect only if your trunk branch group has a frequency of more than 1. It also impacts the spread of leaves if you attached a leaf group to the trunk.  
**Ground Offset** | Lowers the tree relative to the Tree **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)’s y-axis. In other words, the tree
can extend below its GameObject. Use this to sink the tree partially into the
ground, for example to partially cover its roots.  
  
## Geometry

**Property** | **Function**  
---|---  
****LOD** The _Level Of Detail_ (LOD) technique is an optimization that
reduces the number of triangles that Unity has to render for a GameObject when
its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) Quality** | Default level of detail (LOD) for the entire tree. Note that you can change the value for specific branch groups. The higher the LOD, the more complex the tree and the higher its performance impact. The **Hierarchy Stats** field in the **Tree hierarchy** view shows the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh)’s complexity as a count of vertices and
triangles.  
****Ambient Occlusion** A method to approximate how much ambient light (light
not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](Glossary.html#Ambientocclusion)** | Ambient occlusion makes a tree more realistic by creating soft shadows where the tree, branches, and leaves obscures some light. It’s enabled by default, but you can disable it to improve performance.  
**AO Density** | Density of the ambient occlusion, from 0 to 1. The higher the density, the more detailed the shadows, but at the cost of increased memory use.  
  
## Material

**Property** | **Function**  
---|---  
**Translucency Color** | A color multiplier to tint backlit leaves. It simulates the light coming through and creating a halo around the leaves. You might need to rotate your view around your tree to notice the impact, placing the tree between your view and the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene)’s light source.  
**Trans. View Dep.** | Translucency View Dependency. Determines how much the translucency depends on either the view angle or the leaf’s normal vector. When the value is 0, the translucency remains constant even if the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) tilts up or down. If the value is 1,
the translucency changes when the camera tilts.  
**Alpha Cutoff** | Clips alpha values in the texture that are lower than this value. This creates a cutout in the texture. Note that the materials also have an Alpha Cutoff property, and you might need to adjust both cutoffs to get the desired appearance.  
**Shadow Strength** | A shadow multiplier softening the leaves on shadows. Note that this softens all shadows, including those cast by large objects such as neighboring trees and mountains, and so can create shadows that appear too light for their surroundings.  
**Shadow Offset** | Scales the values of the material’s Shadow Offset texture. This offsets the position of the leaves when collecting shadows, so that the leaves don’t look like they were placed on one **quad** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](PrimitiveObjects.html)  
See in [Glossary](Glossary.html#Quad). **Billboard** A textured 2D object that
rotates so that it always faces the Camera. [More info](class-
BillboardRenderer.html)  
See in [Glossary](Glossary.html#Billboard) leaves must always have brighter
values in the center of the texture and darker ones at the border.  
**Shadow Caster Res.** | The resolution of the texture atlas that has alpha values from source diffuse textures. The Unity Editor uses the atlas when rendering leaves that cast shadows. Higher resolutions can impact performance.  
  
## Additional resources

  * [Mesh Renderer component](class-MeshRenderer.html)
  * [Animate trees with Wind Zones](class-WindZone.html)
  * [Create trees and leaves from meshes](terrain-Tree-From-Mesh.html)

[](terrain-Tree-Hierarchy-UI.html)

Tree Hierarchy view UI reference

[](tree-Branches.html)

Branch group reference

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

