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

#  [SystemInfo](SystemInfo.html).GetCompatibleFormat

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

public static
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
GetCompatibleFormat([Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
format,
[Experimental.Rendering.GraphicsFormatUsage](Experimental.Rendering.GraphicsFormatUsage.html)
usage);

### Parameters

format | The [GraphicsFormat](Experimental.Rendering.GraphicsFormat.html) format to look up.  
---|---  
usage | The [GraphicsFormatUsage](Experimental.Rendering.GraphicsFormatUsage.html) usage to look up.  
  
### Returns

**GraphicsFormat** Returns a format supported by the platform. If no
equivalent or compatible format is supported, the function returns
GraphicsFormat.None.

### Description

Returns a format supported by the platform for the specified usage.

If the platform supports the specified format for the usage, this method
returns the input format. Otherwise, the method searches for a supported
format with similar properties to the input format. If the platform doesn't
support any similar format, the method returns a fallback format. For example,
if the input format is a compressed format that isn't supported, the function
returns an uncompressed equivalent format. If the platform doesn't support any
equivalent or compatible fallback formats, this method returns
GraphicsFormat.None.  
  
Additional resources:
[GraphicsFormat](Experimental.Rendering.GraphicsFormat.html) enum and
[GraphicsFormatUsage](Experimental.Rendering.GraphicsFormatUsage.html) flags.

* * *

**Obsolete** Use overload with a GraphicsFormatUsage parameter instead.

## Declaration

public static
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
GetCompatibleFormat([Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
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

