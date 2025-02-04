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

# RenderPickingResult

struct in UnityEditor

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

This struct contains information to notify Unity the outcome of this render
picking callback.

This struct type has to be returned from the
[RenderPickingCallback](HandleUtility.RenderPickingCallback.html) to notify
Unity of:

  * The number of consecutive picking indices used during the callback
  * The [ResolvePickingCallback](HandleUtility.ResolvePickingCallback.html) delegate to invoke when the user clicks on a pixel, whose value is the `selectionId` encoded from the picking index used during the callback. Refer to [resolver](RenderPickingResult-resolver.html) for more information.
  * Alternatively, you can use a [ResolvePickingWithWorldPositionCallback](HandleUtility.ResolvePickingWithWorldPositionCallback.html) delegate if you need the world space position or the depth value for the resolve callback to work. Refer to [resolverWithWorldPos](RenderPickingResult-resolverWithWorldPos.html).

If nothing has been rendered, return
[RenderPickingResult.NoOperation](RenderPickingResult.NoOperation.html).

### Static Properties

[NoOperation](RenderPickingResult.NoOperation.html)| The constant value to be
returned from RenderPickingCallback delegates signifying that nothing has been
rendered.  
---|---  
  
### Properties

[renderedPickingIndexCount](RenderPickingResult-
renderedPickingIndexCount.html)| The number of consecutive picking indices
used during the current RenderPickingCallback.  
---|---  
[resolver](RenderPickingResult-resolver.html)| The callback to invoke to
resolve a picking index into a GameObject reference.  
[resolverWithWorldPos](RenderPickingResult-resolverWithWorldPos.html)| The
callback to invoke to resolve a picking index into a GameObject reference.  
  
### Constructors

[RenderPickingResult](RenderPickingResult-ctor.html)| Constructs a
RenderPickingResult value.  
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

