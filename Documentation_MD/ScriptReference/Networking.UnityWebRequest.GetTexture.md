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

**Removed**  

#  [UnityWebRequest](Networking.UnityWebRequest.html).GetTexture

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

**Obsolete** UnityWebRequest.GetTexture is obsolete. Use
UnityWebRequestTexture.GetTexture instead.  
**Upgrade to[GetTexture](Networking.UnityWebRequestTexture.GetTexture.html)**

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetTexture(string uri);

**Obsolete** UnityWebRequest.GetTexture is obsolete. Use
UnityWebRequestTexture.GetTexture instead.  
**Upgrade to[GetTexture](Networking.UnityWebRequestTexture.GetTexture.html)**

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetTexture(string uri, bool nonReadable);

### Parameters

uri | The URI of the image to download.  
---|---  
nonReadable | If true, the texture's raw data will not be accessible to script. This can conserve memory. Default: `false`.  
  
### Returns

**UnityWebRequest** A [UnityWebRequest](Networking.UnityWebRequest.html)
properly configured to download an image and convert it to a
[Texture](Texture.html).

### Description

Creates a [UnityWebRequest](Networking.UnityWebRequest.html) intended to
download an image via HTTP GET and create a [Texture](Texture.html) based on
the retrieved data.

**Obsolete** \- instead use
[UnityWebRequestTexture.GetTexture](Networking.UnityWebRequestTexture.GetTexture.html).  
  
This method creates a [UnityWebRequest](Networking.UnityWebRequest.html) and
sets the target URL to the string `uri` argument. This method sets no other
flags or custom headers.  
  
This method attaches a
[DownloadHandlerTexture](Networking.DownloadHandlerTexture.html) object to the
[UnityWebRequest](Networking.UnityWebRequest.html).
[DownloadHandlerTexture](Networking.DownloadHandlerTexture.html) is a
specialized [DownloadHandler](Networking.DownloadHandler.html) which is
optimized for storing images which are to be used as textures in the Unity
Engine. Using this class significantly reduces memory reallocation compared to
downloading raw bytes and creating a texture manually in script. In addition,
texture conversion will be performed on a worker thread.  
  
This method attaches no [UploadHandler](Networking.UploadHandler.html) to the
[UnityWebRequest](Networking.UnityWebRequest.html).  
  
UnityWebRequest.GetTexture is obsolete. Use UnityWebRequestTexture.GetTexture
instead.

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

