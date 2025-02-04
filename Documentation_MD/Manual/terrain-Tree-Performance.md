[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-Tree-Performance.html)
  * [中文](/cn/current/Manual/terrain-Tree-Performance.html)
  * [日本語](/ja/current/Manual/terrain-Tree-Performance.html)
  * [한국어](/kr/current/Manual/terrain-Tree-Performance.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-Tree-Performance.html)
  * [中文](/cn/current/Manual/terrain-Tree-Performance.html)
  * [日本語](/ja/current/Manual/terrain-Tree-Performance.html)
  * [한국어](/kr/current/Manual/terrain-Tree-Performance.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](class-Tree.html)
  * Performance tips for trees

[](terrain-Tree-From-Mesh.html)

Create trees and leaves from meshes

[](terrain-Tree-Hierarchy-UI.html)

Tree Hierarchy view UI reference

# Performance tips for trees

To improve the performance of trees:

  * Performance depends on the polygon count of your tree model. Test your trees on your platform, and create simpler trees if performance is low.
  * Don’t create too many leaves and branches, because this can reduce performance.
  * Each **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) tile has settings for tree drawing,
such as the distance from the **camera** A component which creates an image of
a particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) where trees switch to **billboard** A
textured 2D object that rotates so that it always faces the Camera. [More
info](class-BillboardRenderer.html)  
See in [Glossary](Glossary.html#Billboard) mode. These settings can impact the
gaming experience when they create transitions that are visible to the player.
Refer to the [Terrain Settings reference](terrain-OtherSettings.html) for more
information.

## Additional resources

  * [Tree level of detail (LOD)](terrain-Tree-LOD.html)
  * [Shaders and the Ambient-Occlusion folder](terrain-Trees-Mat-Shaders.html)
  * [Tree Hierarchy view UI reference](terrain-Tree-Hierarchy-UI.html)
  * [Root node reference](tree-Root-Node.html)
  * [Branch group reference](tree-Branches.html)
  * [Leaf group reference](tree-Leaves.html)
  * [Terrain Settings reference](terrain-OtherSettings.html)

[](terrain-Tree-From-Mesh.html)

Create trees and leaves from meshes

[](terrain-Tree-Hierarchy-UI.html)

Tree Hierarchy view UI reference

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

