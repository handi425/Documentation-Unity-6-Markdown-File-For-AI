[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/importing-lod-meshes.html)
  * [中文](/cn/current/Manual/importing-lod-meshes.html)
  * [日本語](/ja/current/Manual/importing-lod-meshes.html)
  * [한국어](/kr/current/Manual/importing-lod-meshes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/importing-lod-meshes.html)
  * [中文](/cn/current/Manual/importing-lod-meshes.html)
  * [日本語](/ja/current/Manual/importing-lod-meshes.html)
  * [한국어](/kr/current/Manual/importing-lod-meshes.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](simplifying-distant-meshes-with-level-of-detail-lod.html)
  * Import a mesh with LOD settings

[](configure-mesh-lod.html)

Configure mesh LOD

[](class-LODGroup.html)

LOD Group component reference

# Import a mesh with LOD settings

You can create meshes with different levels of detail in an external 3D
application for use with Unity’s [LOD
system](https://docs.unity3d.com/Manual/LevelOfDetail.html). If you name these
meshes correctly, Unity automatically creates and configures a **GameObject**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with [LOD
group](https://docs.unity3d.com/Manual/class-LODGroup.html)A component to
manage level of detail (LOD) for GameObjects. [More info](class-LODGroup.html)  
See in [Glossary](Glossary.html#LODGroup) component for them when it imports
the Model.

To import a Model with **LOD** The _Level Of Detail_ (LOD) technique is an
optimization that reduces the number of triangles that Unity has to render for
a GameObject when its distance from the Camera increases. [More
info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) level into Unity, you must do the
following:

  1. In your external 3D application, follow the application’s process to create as many LOD meshes as you need.
  2. Name the meshes according to the following naming convention: 
     * ExampleMeshName_LOD0 for the first LOD level (i.e., the most detailed version)
     * ExampleMeshName_LOD1
     * ExampleMeshName_LOD2
  3. Export your Model as an FBX file. Alternatively, if you are using Maya, export the mesh group directly into Unity; to do this, go to **File > Send to Unity > Selection.**
  4. Import the FBX into Unity. Unity recognizes the grouped Meshes and naming convention, and automatically creates an[ LOD Group](https://docs.unity3d.com/Manual/class-LODGroup.html) component with the appropriate settings.

## Additional resources

  * To learn more about importing models, see [Importing models](https://docs.unity3d.com/Manual/ImportingModelFiles.html).
  * To learn more about creating and exporting LOD Meshes in Maya, follow the Unity tutorial [Creating LODs in Maya](https://learn.unity.com/tutorial/creating-lods-in-maya-for-unity).

[](configure-mesh-lod.html)

Configure mesh LOD

[](class-LODGroup.html)

LOD Group component reference

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

