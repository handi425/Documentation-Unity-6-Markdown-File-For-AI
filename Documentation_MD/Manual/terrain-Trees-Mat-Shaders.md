[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/terrain-Trees-Mat-Shaders.html)
  * [中文](/cn/current/Manual/terrain-Trees-Mat-Shaders.html)
  * [日本語](/ja/current/Manual/terrain-Trees-Mat-Shaders.html)
  * [한국어](/kr/current/Manual/terrain-Trees-Mat-Shaders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/terrain-Trees-Mat-Shaders.html)
  * [中文](/cn/current/Manual/terrain-Trees-Mat-Shaders.html)
  * [日本語](/ja/current/Manual/terrain-Trees-Mat-Shaders.html)
  * [한국어](/kr/current/Manual/terrain-Trees-Mat-Shaders.html)

  * [World building](CreatingEnvironments.html)
  * [Terrain](script-Terrain.html)
  * [Trees](terrain-Trees-Landing.html)
  * [Create trees with Tree Editor](class-Tree.html)
  * Shaders and the Ambient-Occlusion folder

[](tree-Structure.html)

Tree Editor concepts

[](tree-FirstTree.html)

Design a tree

# Shaders and the Ambient-Occlusion folder

Trees you create using Tree Editor must use the **Nature/Soft Occlusion
Leaves** and **Nature/Soft Occlusion Bark** **shaders** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

To use these shaders, you must place your trees in a folder named `Ambient-
Occlusion`. The trees don’t render correctly if the shaders are in a different
folder.

To place trees in the `Ambient-Occlusion` folder:

  1. In the **Project** window, select the `Assets` folder.
  2. Select **Add** (+) > **Folder**.
  3. Give the folder the name `Ambient-Occlusion`.
  4. Move the tree **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) (`Tree.prefab`) and its texture folder
(`Tree_Textures`) into the `Ambient-Occlusion` folder. These objects were
created when you added a Tree **GameObject** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to your **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

**Note** : The dependency on these shaders means you can only use Tree Editor
trees with the Built-In **Render Pipeline** A series of operations that take
the contents of a Scene, and displays them on a screen. Unity lets you choose
from pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline). If you’re using the Universal
Render Pipeline (URP) or High Definition Render Pipeline (HDRP), you can
import trees from [SpeedTree](SpeedTree-landing.html).

## Additional resources

  * [Tree level of detail (LOD)](terrain-Tree-LOD.html)
  * [Tree Hierarchy view UI reference](terrain-Tree-Hierarchy-UI.html)
  * [Root node reference](tree-Root-Node.html)
  * [Branch group reference](tree-Branches.html)
  * [Leaf group reference](tree-Leaves.html)
  * [Terrain Settings reference](terrain-OtherSettings.html)

[](tree-Structure.html)

Tree Editor concepts

[](tree-FirstTree.html)

Design a tree

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

