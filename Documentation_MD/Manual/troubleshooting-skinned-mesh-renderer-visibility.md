[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)
  * [中文](/cn/current/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)
  * [日本語](/ja/current/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)
  * [한국어](/kr/current/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)
  * [中文](/cn/current/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)
  * [日本語](/ja/current/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)
  * [한국어](/kr/current/Manual/troubleshooting-skinned-mesh-renderer-visibility.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * Troubleshooting Skinned Mesh Renderer visibility

[](class-Mesh.html)

Mesh asset Inspector window reference

[](Prefabs.html)

Prefabs

# Troubleshooting Skinned Mesh Renderer visibility

Unity uses the **mesh** The main graphics primitive of Unity. Meshes make up a
large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh)’s bounds to determine whether to render
it. If the entire **bounding volume** A closed shape representing the edges
and faces of a collider or trigger.  
See in [Glossary](Glossary.html#Boundingvolume) is outside the view of any
active **Camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), Unity does not render the mesh.

In the case of a Skinned **Mesh Renderer** A mesh component that takes the
geometry from the Mesh Filter and renders it at the position defined by the
object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer), its mesh bounds change as it
deforms. Unity accounts for all animations present at import time when it
calculates the maximum bounding volume, and uses this value to determine
visibility; however, the following situations that occur after import might
push vertices or bones outside of the maximum known bounds:

  * Additive animations
  * Changing the positions of bones from a script at runtime
  * Using vertex **shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that change vertex positions

  * Using ragdolls

If this happens, Unity might not correctly determine the visibility of the
mesh, and might fail to show it when expected.

In these cases, you can try either of the following solutions to fix the
problem:

  * Modify the bounds to match the maximum potential bounding volume of your mesh. Use this option if possible, because it is better for performance.
  * Enable **Update When Offscreen** , so that Unity continues to calculate the mesh bounds at all times, even when the mesh is not visible. Use this option if performance is not a major concern, or if you can’t predict the size of your bounding volume (for example, if you use ragdolls).

[](class-Mesh.html)

Mesh asset Inspector window reference

[](Prefabs.html)

Prefabs

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

