[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# RenderParams

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Rendering parameters used by various rendering functions.

This struct defines common parameters shared across various rendering
functions.  
  
Additional resources: [Graphics.RenderMesh](Graphics.RenderMesh.html),
[Graphics.RenderMeshInstanced](Graphics.RenderMeshInstanced.html),
[Graphics.RenderMeshIndirect](Graphics.RenderMeshIndirect.html),
[Graphics.RenderMeshPrimitives](Graphics.RenderMeshPrimitives.html),
[Graphics.RenderPrimitives](Graphics.RenderPrimitives.html),
[Graphics.RenderPrimitivesIndexed](Graphics.RenderPrimitivesIndexed.html),
[Graphics.RenderPrimitivesIndirect](Graphics.RenderPrimitivesIndirect.html),
[Graphics.RenderPrimitivesIndexedIndirect](Graphics.RenderPrimitivesIndexedIndirect.html).

### Properties

[camera](RenderParams-camera.html)| The camera used for rendering. If set to
null (default) renders for all cameras.  
---|---  
[instanceID](RenderParams-instanceID.html)| The instance ID of the GameObject
that issues the draw. Provide an instanceID to make a rendered GameObject
pickable in the scene view when you click on it. The default value is 0, which
means that you can't pick or outline the procedural GameObject in the scene
view.  
[layer](RenderParams-layer.html)| Layer used for rendering. Layer to use.  
[lightProbeProxyVolume](RenderParams-lightProbeProxyVolume.html)| Light Probe
Proxy Volume (LPPV) used for rendering.  
[lightProbeUsage](RenderParams-lightProbeUsage.html)| The type of light probe
usage.  
[material](RenderParams-material.html)| Material used for rendering.  
[matProps](RenderParams-matProps.html)| Material properties used for
rendering.  
[motionVectorMode](RenderParams-motionVectorMode.html)| Motion vector mode
used for rendering.  
[overrideSceneCullingMask](RenderParams-overrideSceneCullingMask.html)| Uses
the RenderParams.sceneCullingMask property to specify a custom
SceneCullingMasks. This property is only available in the Editor, you can
still access it in a Player but it'll be ignored.  
[receiveShadows](RenderParams-receiveShadows.html)| Descripes if the rendered
geometry should receive shadows.  
[reflectionProbeUsage](RenderParams-reflectionProbeUsage.html)| The type of
reflection probe used for rendering.  
[rendererPriority](RenderParams-rendererPriority.html)| Renderer priority.  
[renderingLayerMask](RenderParams-renderingLayerMask.html)| Renderer layer
mask used for rendering.  
[sceneCullingMask](RenderParams-sceneCullingMask.html)| Overrides the scene
culling mask for the rendered object. This can help you control prefab stage
visibility or entities sub-scene visibiliy. This property is only available in
the Editor, you can still access it in a Player but it'll be ignored..  
[shadowCastingMode](RenderParams-shadowCastingMode.html)| Describes if
geometry should cast shadows.  
[worldBounds](RenderParams-worldBounds.html)| Defines world space bounds for
the geometry. Used to cull and sort the rendered geometry.  
  
### Constructors

[RenderParams](RenderParams-ctor.html)| Constructor.  
---|---  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

