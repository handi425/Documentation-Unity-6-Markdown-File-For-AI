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

# AttachmentDescriptor

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

A declaration of a single color or depth rendering surface to be attached into
a RenderPass.

A AttachmentDescriptor object identifies a single color or depth rendering
surface that can be used with a RenderPass. Note that the AttachmentDescriptor
object derives from UnityEngine.Object so they do not get garbage collected
like normal C# objects. Instead, they are only GC'd when unloading a Scene or
when Resources.UnloadUnusedAssets() is called. Therefore do not create these
objects each frame: Instead, create these objects in the constructor of your
rendering class, and reuse those objects each frame.

### Properties

[clearColor](Rendering.AttachmentDescriptor-clearColor.html)| The currently
assigned clear color for this attachment. Default is black.  
---|---  
[clearDepth](Rendering.AttachmentDescriptor-clearDepth.html)| Currently
assigned depth clear value for this attachment. Default value is 1.0.  
[clearStencil](Rendering.AttachmentDescriptor-clearStencil.html)| Currently
assigned stencil clear value for this attachment. Default is 0.  
[format](Rendering.AttachmentDescriptor-format.html)| The format of this
attachment.  
[graphicsFormat](Rendering.AttachmentDescriptor-graphicsFormat.html)| The
GraphicsFormat of this attachment. To use in place of format.  
[loadAction](Rendering.AttachmentDescriptor-loadAction.html)| The load action
to be used on this attachment when the RenderPass starts.  
[loadStoreTarget](Rendering.AttachmentDescriptor-loadStoreTarget.html)| The
surface to use as the backing storage for this AttachmentDescriptor.  
[resolveTarget](Rendering.AttachmentDescriptor-resolveTarget.html)| When the
renderpass that uses this attachment ends, resolve the MSAA surface into the
given target.  
[storeAction](Rendering.AttachmentDescriptor-storeAction.html)| The store
action to use with this attachment when the RenderPass ends. Only used when
either ConfigureTarget or ConfigureResolveTarget has been called.  
  
### Constructors

[AttachmentDescriptor](Rendering.AttachmentDescriptor-ctor.html)| Create a
AttachmentDescriptor to be used with RenderPass.  
---|---  
  
### Public Methods

[ConfigureClear](Rendering.AttachmentDescriptor.ConfigureClear.html)| When the
RenderPass starts, clear this attachment into the color or depth/stencil
values given (depending on the format of this attachment). Changes loadAction
to RenderBufferLoadAction.Clear.  
---|---  
[ConfigureResolveTarget](Rendering.AttachmentDescriptor.ConfigureResolveTarget.html)|
When the renderpass that uses this attachment ends, resolve the MSAA surface
into the given target.  
[ConfigureTarget](Rendering.AttachmentDescriptor.ConfigureTarget.html)| Binds
this AttachmentDescriptor to the given target surface.  
  
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

