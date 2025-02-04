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

#  [RenderPickingResult](RenderPickingResult.html).resolver

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

public
[HandleUtility.ResolvePickingCallback](HandleUtility.ResolvePickingCallback.html)
resolver;

### Description

The callback to invoke to resolve a picking index into a GameObject reference.

The callback is invoked only if one of the picking indices rendered ends up
being the topmost one under the mouse click position.  
  
The callback is provided with a local picking index: the 0-based index that is
offset from picking indices you used for rendering by subtracting
[RenderPickingArgs.pickingIndex](RenderPickingArgs-pickingIndex.html).  
  
The callback returns a [GameObject](GameObject.html) reference from the given
arguments. If you need more contextual data for the resolve callback to work,
you can construct the callback as a lambda function from the render callback
so that you can capture variables such as `pickingIndex` into it.  
  
Returns null if the picking index doesn't resolve to any GameObject. This
signals Unity to end the picking loop (for finding all objects under the
mouse) and to start over.  
  
Additional resources:
[RenderPickingResult.resolverWithWorldPos](RenderPickingResult-
resolverWithWorldPos.html).

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

