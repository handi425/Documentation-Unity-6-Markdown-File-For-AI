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

#  [UnityWebRequest](Networking.UnityWebRequest.html).url

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

public string url;

### Description

Defines the target URL for the
[UnityWebRequest](Networking.UnityWebRequest.html) to communicate with.

This property cannot be set after calling
[SendWebRequest](Networking.UnityWebRequest.SendWebRequest.html).  
  
If the [UnityWebRequest](Networking.UnityWebRequest.html) encounters and
follows redirects, this property will be updated with the URL to which the
[UnityWebRequest](Networking.UnityWebRequest.html) was redirected.  
  
When inputting URLs, absolute URLs are preferred. However, if you input a
partial URL, the system will follow these rules:  
  
**If the input URL starts with two slashes (//)** , then the input is assumed
to be a domain and path intended for use over HTTPS.  
  
On non-WebGL platforms, the system will prepend _https:_. On WebGL, the system
will inherit the scheme of the path by which the Unity WebGL application is
being accessed.  
  
Examples: If the WebGL app is being accessed via https, the system will
prepend _https:_. If the WebGL app is being accessed via http, the system will
prepend _http:_.  
  
**If the input URL starts with a single slash (/)** , then the system assumes
the inout is a path relative to the current domain on which the Unity
application is running. On non-WebGL platforms, the system will prepend
_https://localhost_ to the URL.  
  
On WebGL, the system will prepend the scheme and host of the path by which the
Unity WebGL application is being accessed. For example, if the Unity WebGL app
is being accessed via _https://unity3d.com/myapp_ , then the system will
prepend _https://unity3d.com_ to relative paths.  
  
**If neither of the above rules apply** , the system validates your input
string via the built-in [System.Uri](https://msdn.microsoft.com/en-
us/library/system.uri) class. If this class throws a
[URIFormatException](https://msdn.microsoft.com/en-
us/library/system.uriformatexception), the system attempts to append the input
string to the absolute URL by which the Unity app is being accessed. (see
above)  
  
Any further exceptions will be re-thrown.

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

