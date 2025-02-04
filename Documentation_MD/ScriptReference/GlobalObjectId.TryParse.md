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

#  [GlobalObjectId](GlobalObjectId.html).TryParse

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

public static bool TryParse(string stringValue, out
[GlobalObjectId](GlobalObjectId.html) id);

### Parameters

stringValue | The string representation of a `GlobalObjectId`.  
  
The following is an example of the string representation:
`GlobalObjectId_V1-2-74c253e3f16be4776bb2d88e01f77c8a-902906726-0`. For more
information on the composition, refer to
[GlobalObjectId](GlobalObjectId.html).  
---|---  
id | The `GlobalObjectId` struct to populate with the parsed values.  
  
### Returns

**bool** Returns `true` if the string representation is successfully parsed.
Otherwise, returns `false`

### Description

Tries to parse the string representation of a GlobalObjectId into a
GlobalObjectId struct.

This method takes the string representation of a unique object identifier and
converts it to a `GlobalObjectId` struct.  
  
Calling this method sets the state of the provided `GlobalObjectId`, but
doesn't attempt to resolve it to an object reference. A return value of `true`
doesn't guarantee that a call to
[GlobalObjectId.GlobalObjectIdentifierToObjectSlow](GlobalObjectId.GlobalObjectIdentifierToObjectSlow.html)
or similar method will succeed.  
  
Additional resources: [GlobalObjectId.ToString](GlobalObjectId.ToString.html)

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

