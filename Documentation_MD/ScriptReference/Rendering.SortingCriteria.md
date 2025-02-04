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

# SortingCriteria

enumeration

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

How to sort objects during rendering.

Control the way Unity sorts objects before drawing them by using and combining
these flags.  
  
The basic flags are:

  * [SortingLayer](Rendering.SortingCriteria.SortingLayer.html),
  * [RenderQueue](Rendering.SortingCriteria.RenderQueue.html),
  * [BackToFront](Rendering.SortingCriteria.BackToFront.html),
  * [QuantizedFrontToBack](Rendering.SortingCriteria.QuantizedFrontToBack.html),
  * [OptimizeStateChanges](Rendering.SortingCriteria.OptimizeStateChanges.html),
  * [CanvasOrder](Rendering.SortingCriteria.CanvasOrder.html).

Multiple flags, when combined, are applied in the above order.  
  
Some commonly-used sorting combinations are provided for convenience. Use
[CommonOpaque](Rendering.SortingCriteria.CommonOpaque.html) for opaque
objects. This combination of flags includes optimization for reducing draw
state changes and draws roughly front-to-back to reduce drawing over the same
pixels many times. Use
[CommonTransparent](Rendering.SortingCriteria.CommonTransparent.html) for
transparent objects, which need to be sorted from back to front before being
drawn for them all to be visible.  
  
Additional resources: DrawingSettings.sorting,
ScriptableRenderContext.DrawRenderers.

### Properties

[None](Rendering.SortingCriteria.None.html)| Do not sort objects.  
---|---  
[SortingLayer](Rendering.SortingCriteria.SortingLayer.html)| Sort by renderer
sorting layer.  
[RenderQueue](Rendering.SortingCriteria.RenderQueue.html)| Sort by material
render queue.  
[BackToFront](Rendering.SortingCriteria.BackToFront.html)| Sort objects back
to front.  
[QuantizedFrontToBack](Rendering.SortingCriteria.QuantizedFrontToBack.html)|
Sort objects in rough front-to-back buckets.  
[OptimizeStateChanges](Rendering.SortingCriteria.OptimizeStateChanges.html)|
Sort objects to reduce draw state changes.  
[CanvasOrder](Rendering.SortingCriteria.CanvasOrder.html)| Sort renderers
taking canvas order into account.  
[RendererPriority](Rendering.SortingCriteria.RendererPriority.html)| Sorts
objects by renderer priority.  
[CommonOpaque](Rendering.SortingCriteria.CommonOpaque.html)| Typical sorting
for opaque objects.  
[CommonTransparent](Rendering.SortingCriteria.CommonTransparent.html)| Typical
sorting for transparencies.  
  
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

