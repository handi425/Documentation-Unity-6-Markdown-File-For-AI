[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/motion-vectors-reference.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-reference.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-reference.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/motion-vectors-reference.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-reference.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-reference.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Motion vectors in URP](../../urp/features/motion-vectors-landing.html)
  * Motion vectors settings reference for URP

[](../../urp/features/motion-vectors-troubleshooting.html)

Troubleshooting motion vectors in URP

[](../../urp/change-resolution-scale-urp.html)

Upscaling resolution in URP with Spatial-Temporal Post-Processing

# Motion vectors settings reference for URP

To specify how a GameObject contributes to the motion vector buffer, use the
**Motion Vectors** property: **Mesh Renderer** >> **Additional Settings** >>
**Motion Vectors**. This property lets you disable motion vector rendering for
a specific object, or fill the motion vector texture with zeros for the
visible fragments of the object’s renderer.

The following table describes the available **Motion Vectors** property
options.

**Motion Vectors** option | Description  
---|---  
**Camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) Motion Only | Unity treats the object as stationary in the world when rendering camera motion vectors. Unity does not draw a per-object motion vector pass for this MeshRenderer. If motion vector rendering is a GPU bottleneck, you can use this option as an optimization for objects which move slowly.  
Per Object Motion | Unity renders the per-object **Motion Vectors** pass for this object.  
Force No Motion | Unity renders the per-object **Motion Vectors** pass every frame for this object, but sets a special shader uniform variable to tell the pass to skip calculations and to write zero values. A per-object pass is still necessary to overwrite any non-zero camera motion vectors from the full-screen pass.  
You can use this option to avoid artefacts from the camera motion blur on a 3D
HUD, or a third person character, or a race car, or if you have some other
artefacts related to incorrect motion vectors on an object that you would like
to avoid.  
  
[](../../urp/features/motion-vectors-troubleshooting.html)

Troubleshooting motion vectors in URP

[](../../urp/change-resolution-scale-urp.html)

Upscaling resolution in URP with Spatial-Temporal Post-Processing

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

