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

# FilteringSettings

struct in UnityEngine.Rendering

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

A struct that represents filtering settings for
ScriptableRenderContext.DrawRenderers.

A `FilteringSettings` struct describes how to filter the set of objects that
ScriptableRenderContext.DrawRenderers receives, so that Unity draws a subset
of them.  
  
Additional resources: ScriptableRenderContext.DrawRenderers, [Creating a
simple render loop in a custom render pipeline](../Manual/srp-creating-simple-
render-loop.html).

### Static Properties

[defaultValue](Rendering.FilteringSettings-defaultValue.html)| Creates a
FilteringSettings struct that contains default values for all properties. With
these default values, Unity does not perform any filtering.  
---|---  
  
### Properties

[batchLayerMask](Rendering.FilteringSettings-batchLayerMask.html)| Represents
which BatchRendererGroup batch layers to enable for rendering.  
---|---  
[excludeMotionVectorObjects](Rendering.FilteringSettings-
excludeMotionVectorObjects.html)| Determines if Unity excludes GameObjects
that are in motion from rendering. This refers to GameObjects that have an
active Motion Vector pass assigned to their Material or have set the Motion
Vector mode to per object motion (Menu: Mesh Renderer > Additional Settings >
Motion Vectors > Per Object Motion). For Unity to exclude a GameObject from
rendering, the GameObject must have moved since the last frame. To exclude a
GameObject manually, enable a Motion Vector pass.  
[forceAllMotionVectorObjects](Rendering.FilteringSettings-
forceAllMotionVectorObjects.html)| Determines if Unity renders not moving
GameObjects in motion vector pass. This refers to GameObjects that have an
active Motion Vector pass assigned to their Material and did not move since
the last frame. This flag can be used to render both moving objects and not
moving objects in the motion vector pass to populate object motion data and
scene depth data together.  
[layerMask](Rendering.FilteringSettings-layerMask.html)| Unity renders objects
whose GameObject.layer value is enabled in this bit mask.  
[renderingLayerMask](Rendering.FilteringSettings-renderingLayerMask.html)|
Unity renders objects whose Renderer.renderingLayerMask value is enabled in
this bit mask.  
[renderQueueRange](Rendering.FilteringSettings-renderQueueRange.html)| Unity
renders objects whose Material.renderQueue value is within range specified by
this RenderQueueRange.  
[sortingLayerRange](Rendering.FilteringSettings-sortingLayerRange.html)| Unity
renders objects whose SortingLayer.value value is within range specified by
this SortingLayerRange.  
  
### Constructors

[FilteringSettings](Rendering.FilteringSettings-ctor.html)| Creates a
FilteringSettings struct for use with
Rendering.ScriptableRenderContext.DrawRenderers.  
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

