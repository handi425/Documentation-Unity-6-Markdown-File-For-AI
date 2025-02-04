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

#  [SystemInfo](SystemInfo.html).IsFormatSupported

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

public static bool
IsFormatSupported([Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
format,
[Experimental.Rendering.GraphicsFormatUsage](Experimental.Rendering.GraphicsFormatUsage.html)
usage);

### Parameters

format | The [GraphicsFormat](Experimental.Rendering.GraphicsFormat.html) format to look up.  
---|---  
usage | The [GraphicsFormatUsage](Experimental.Rendering.GraphicsFormatUsage.html) usage to look up.  
  
### Returns

**bool** Returns true if the format is supported for the specific usage.
Returns false otherwise.

### Description

Verifies that the specified graphics format is supported for the specified
usage.

If a specific usage is not supported by a format, the operation will fail.  
  
Additional resources:
[GraphicsFormat](Experimental.Rendering.GraphicsFormat.html) enum and
[GraphicsFormatUsage](Experimental.Rendering.GraphicsFormatUsage.html) flags.

* * *

**Obsolete** Use overload with a GraphicsFormatUsage parameter instead.

## Declaration

public static bool
IsFormatSupported([Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
format, FormatUsage usage);

### Description

Obsolete. Use the overload with a
[GraphicsFormatUsage](Experimental.Rendering.GraphicsFormatUsage.html)
parameter instead.

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

