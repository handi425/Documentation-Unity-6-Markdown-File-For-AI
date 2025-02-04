[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/mesh-introduction.html)
  * [中文](/cn/current/Manual/mesh-introduction.html)
  * [日本語](/ja/current/Manual/mesh-introduction.html)
  * [한국어](/kr/current/Manual/mesh-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/mesh-introduction.html)
  * [中文](/cn/current/Manual/mesh-introduction.html)
  * [日本語](/ja/current/Manual/mesh-introduction.html)
  * [한국어](/kr/current/Manual/mesh-introduction.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Get started with meshes](get-started-with-meshes.html)
  * Introduction to meshes

[](get-started-with-meshes.html)

Get started with meshes

[](AnatomyofaMesh.html)

Mesh data

# Introduction to meshes

A mesh is a collection of data that describes a shape. In Unity, you use
meshes in the following ways:

  * In graphics, you use meshes together with [materials](Materials.html)An asset that defines how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material); meshes describe the shape of an
object that the GPU renders, and materials describe the appearance of its
surface.

  * In physics, you can use a mesh to determine the shape of a **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider).

## Deformable meshes

In addition to regular meshes, Unity also supports deformable meshes.

Deformable meshes fall into the following categories:

  * Skinned meshes: These meshes work with additional data called bones. Bones form a structure called a skeleton (also called a rig, or joint hierarchy), and the skinned mesh contains data that allows it to deform in a realistic way when the skeleton moves. You usually use skinned meshes for [skeletal animation](https://en.wikipedia.org/wiki/Skeletal_animation) with Unity’s [Animation](AnimationSection.html) features, but you can also use them with [Rigidbody components](class-Rigidbody.html) to create “ragdoll” effects.
  * Meshes with blend shapes: These meshes contain data called blend shapes. Blend shapes describe versions of the mesh that are deformed into different shapes, which Unity interpolates between. You use blend shapes for [morph target animation](https://en.wikipedia.org/wiki/Morph_target_animation), which is a common technique for facial animation.
  * Meshes that work with a [Cloth component](class-Cloth.html) component for realistic fabric simulation.

## Working with meshes

Unity stores meshes in your project as [mesh assets](class-Mesh.html), and
represents them in C# code with the [Mesh](../ScriptReference/Mesh.html)The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) class.

Depending on how you use meshes, they work with different components:

  * In graphics, Unity renders regular meshes with [Mesh Renderer](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) components, and deformable
meshes with [Skinned Mesh Renderer](class-SkinnedMeshRenderer.html)
components.

  * In physics, Unity uses the [Mesh Collider](https://docs.unity3d.com/Manual/class-MeshCollider.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](class-MeshCollider.html)  
See in [Glossary](Glossary.html#MeshCollider) component to determine the shape
of a collider.

For detailed information about the data that a mesh contains and how Unity
represents that data, see [Mesh data](AnatomyofaMesh.html).

[](get-started-with-meshes.html)

Get started with meshes

[](AnatomyofaMesh.html)

Mesh data

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

