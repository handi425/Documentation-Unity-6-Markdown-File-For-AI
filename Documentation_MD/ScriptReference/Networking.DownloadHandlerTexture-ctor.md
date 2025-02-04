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

# DownloadHandlerTexture Constructor

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

public DownloadHandlerTexture();

### Description

Default constructor.

Convenience constructor. Assumes the value of `readable` is `false`. The
[Texture](Texture.html) returned by `texture` will not have its texture data
accessible from script.

    
    
    using System.Collections;
    using UnityEngine;
    using UnityEngine.Networking;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator Start()
        {
            using (var uwr = new [UnityWebRequest](Networking.UnityWebRequest.html)("https://website.com/image.jpg", [UnityWebRequest.kHttpVerbGET](Networking.UnityWebRequest-kHttpVerbGET.html)))
            {
                uwr.downloadHandler = new [DownloadHandlerTexture](Networking.DownloadHandlerTexture.html)();
                yield return uwr.SendWebRequest();
                GetComponent<[Renderer](Renderer.html)>().material.mainTexture = [DownloadHandlerTexture.GetContent](Networking.DownloadHandlerTexture.GetContent.html)(uwr);
            }
        }
    }
    

* * *

## Declaration

public DownloadHandlerTexture(bool readable);

### Parameters

readable | Value to set for [TextureImporter.isReadable](TextureImporter-isReadable.html).  
---|---  
  
### Description

Constructor, allows [TextureImporter.isReadable](TextureImporter-
isReadable.html) property to be set.

The value in `readable` will be used to set the
[TextureImporter.isReadable](TextureImporter-isReadable.html) property when
importing the downloaded texture data.

* * *

## Declaration

public
DownloadHandlerTexture([Networking.DownloadedTextureParams](Networking.DownloadedTextureParams.html)
parameters);

### Parameters

parameters | Parameters specifying various properties of texture that will be created.  
---|---  
  
### Description

Constructor that allows you to specify the full set of supported properties
when creating a texture from a downloaded image.

The value of `parameters` allows control of more properties of the texture.
Refer to [Texture2D](Texture2D.html) for more information about texture
properties.

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

