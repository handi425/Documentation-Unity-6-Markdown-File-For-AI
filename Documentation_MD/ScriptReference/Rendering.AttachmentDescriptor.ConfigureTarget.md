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

#  [AttachmentDescriptor](Rendering.AttachmentDescriptor.html).ConfigureTarget

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

## Declaration

public void
ConfigureTarget([Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
target, bool loadExistingContents, bool storeResults);

### Parameters

tgt | The surface to use as the backing storage for this AttachmentDescriptor.  
---|---  
loadExistingContents | Whether to read in the existing contents of the surface when the RenderPass starts.  
storeResults | Whether to store the rendering results of the attachment when the RenderPass ends.  
  
### Description

Binds this AttachmentDescriptor to the given target surface.

This method sets the backing storage of this AttachmentDescriptor to the given
target surface.  
  
If loadExistingContents is true, changes
[loadAction](Rendering.AttachmentDescriptor-loadAction.html) to
RenderBufferStoreAction.Load unless the load action is already set to
RenderBufferStoreAction.Clear, in which case this parameter is ignored.  
  
If `storeResults` is true, changes
[storeAction](Rendering.AttachmentDescriptor-storeAction.html) to either
[RenderBufferStoreAction.Store](Rendering.RenderBufferStoreAction.Store.html)
or
[RenderBufferStoreAction.StoreAndResolve](Rendering.RenderBufferStoreAction.StoreAndResolve.html)
depending on whether the `resolveAttachment` was configured or not.  
  
Note: If you call both
[ConfigureResolveTarget](Rendering.AttachmentDescriptor.ConfigureResolveTarget.html)
with `storeResults` set to `true` and `ConfigureTarget`, Unity stores both the
resolved and unresolved MSAA surfaces respectively in `resolveTarget` and
`loadStoreTarget`. This means Unity writes more data to memory.

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

