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

# TextAsset Constructor

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

[Switch to Manual](../Manual/class-TextAsset.html "Go to TextAsset Component
in the Manual")

## Declaration

public TextAsset(string text);

### Parameters

text | The text contents for the [TextAsset](TextAsset.html).  
---|---  
  
### Description

Creates a new [TextAsset](TextAsset.html) with specified text contents.

This constructor creates a [TextAsset](TextAsset.html), not a plain text file.
To save a [TextAsset](TextAsset.html) to disk using the
[AssetDatabase](AssetDatabase.html) class, save the
[TextAsset](TextAsset.html) with the .asset extension.

* * *

## Declaration

public TextAsset(ReadOnlySpan<byte> bytes);

### Parameters

bytes | The byte contents for the [TextAsset](TextAsset.html).  
---|---  
  
### Description

Creates a new [TextAsset](TextAsset.html) with specified byte contents.

This constructor creates a [TextAsset](TextAsset.html), not a plain text file.
To save a [TextAsset](TextAsset.html) to disk using the
[AssetDatabase](AssetDatabase.html) class, save the
[TextAsset](TextAsset.html) with the .asset extension.  
  
Use this form of the constructor to specify an arbitrary byte buffer to store
in the TextAsset. Use the [TextAsset.bytes](TextAsset-bytes.html) property to
access this data or use the [TextAsset.text](TextAsset-text.html) property to
interpret the byte data as text.

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

