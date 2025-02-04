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

# IMultipartFormSection

interface in UnityEngine.Networking

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

An interface for composition of data into multipart forms.

In order to provide a finer level of control for those wishing to generate
multipart form data, but without forcing most users to refer to [RFC
2388](http://tools.ietf.org/html/rfc2388), Unity provides this simple
interface which the UnityWebRequest API can use to serialize complex data into
properly-formatted bytes.  
  
For convenience, the two general types of form sections have been encapsulated
into two stock implementations of IMultipartFormSection. Both stock
implementations are simply controlled via their constructors.  
  
IMultipartFormSection implementors are converted into bytes via
[UnityWebRequest.SerializeFormSections].  
  
Additional resources: [MultipartFormDataSection], [MultipartFormFileSection].

### Properties

[contentType](Networking.IMultipartFormSection-contentType.html)| Returns the
value to use in the Content-Type header for this form section.  
---|---  
[fileName](Networking.IMultipartFormSection-fileName.html)| Returns a string
denoting the desired filename of this section on the destination server.  
[sectionData](Networking.IMultipartFormSection-sectionData.html)| Returns the
raw binary data contained in this section. Must not return null or a zero-
length array.  
[sectionName](Networking.IMultipartFormSection-sectionName.html)| Returns the
name of this section, if any.  
  
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

