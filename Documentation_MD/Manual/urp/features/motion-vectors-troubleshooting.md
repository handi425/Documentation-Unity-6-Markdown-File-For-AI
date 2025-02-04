[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/motion-vectors-troubleshooting.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-troubleshooting.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-troubleshooting.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-troubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/motion-vectors-troubleshooting.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-troubleshooting.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-troubleshooting.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-troubleshooting.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Motion vectors in URP](../../urp/features/motion-vectors-landing.html)
  * Troubleshooting motion vectors in URP

[](../../urp/features/motion-vectors-sample.html)

Sample motion vectors in a shader in URP

[](../../urp/features/motion-vectors-reference.html)

Motion vectors settings reference for URP

# Troubleshooting motion vectors in URP

Solve common issues with motion vectors in the Universal **Render Pipeline** A
series of operations that take the contents of a Scene, and displays them on a
screen. Unity lets you choose from pre-built render pipelines, or write your
own. [More info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) (URP).

## Fix motion vectors that are too large

If a **camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) is locked to an object that
moves, for example, a model of a car in a racing game, select the **Per Object
Motion** option in the **Motion Vectors** property of that object. If you
don’t select that option, the object will have incorrectly large motion
vectors. This happens because Unity calculates camera motion vectors assuming
that the geometry of the object is static in the world, and that the camera is
moving relative to it. This might cause significant TAA or motion blur
artifacts.

## Fix visual artefacts

When the motion vector texture is used by full-screen **post-processing** A
process that improves product visuals by applying filters and effects before
the image appears on screen. You can use post-processing effects to simulate
physical camera and film properties, for example Bloom and Depth of Field.
[More info](../../PostProcessingOverview.html) post processing,
postprocessing, postprocess  
See in [Glossary](../../Glossary.html#post-processing) effects, such as TAA
and motion blur, any screen regions with incorrect motion vectors (either
missing, or inaccurate) will likely exhibit visual artifacts. The artifacts
can include: texture blurring, movement ghosting, improper anti-aliasing, non-
realistic or inappropriate motion blur, and so on.

If you are experiencing artifacts that you suspect are caused by incorrect
motion vectors, check if the affected objects have object motion vector
rendering enabled. In the **Frame Debugger** , the object should be present in
the **MotionVectors** pass. To troubleshoot missing or incorrect motion
vectors for a particular object, refer to the section [Cases when Unity
renders motion vectors](motion-vectors.html#cases-when-motion-vectors).

[](../../urp/features/motion-vectors-sample.html)

Sample motion vectors in a shader in URP

[](../../urp/features/motion-vectors-reference.html)

Motion vectors settings reference for URP

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

