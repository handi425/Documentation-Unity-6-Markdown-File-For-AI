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

#  [Client](PackageManager.Client.html).Pack

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

[Switch to Manual](../Manual/class-PackageManager.html "Go to PackageManager
Component in the Manual")

## Declaration

public static
[PackageManager.Requests.PackRequest](PackageManager.Requests.PackRequest.html)
Pack(string packageFolder, string targetFolder);

### Parameters

packageFolder | Folder containing the package. `ArgumentException` is thrown if `packageFolder` is `null` or empty.  
---|---  
targetFolder | Folder where the Package Manager will write the GZip tarball file. The Package Manager will create this folder if it does not already exist. `ArgumentException` is thrown if `targetFolder` is `null` or empty.  
  
### Returns

**PackRequest** A [PackRequest](PackageManager.Requests.PackRequest.html)
instance, which you can use to get the
[PackOperationResult](PackageManager.PackOperationResult.html) representing
the path of the generated tarball from the `PackRequest.Result` property.

### Description

Creates a GZip tarball file from a package folder. The format and content of
the file is the same as if the package was published to a package registry.

`Pack()` is an asynchronous operation. Before the operation is complete, you
can use the `PackRequest` instance to monitor the asynchronous operation.  
  
**Note:** Make sure any other Client operations have completed before calling
this method. For more information, see the note on the
[Client](PackageManager.Client.html) class reference page.

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

