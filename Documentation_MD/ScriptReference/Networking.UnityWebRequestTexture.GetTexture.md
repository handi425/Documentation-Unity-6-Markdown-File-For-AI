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

#  [UnityWebRequestTexture](Networking.UnityWebRequestTexture.html).GetTexture

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

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetTexture(string uri);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetTexture(Uri uri);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetTexture(string uri, bool nonReadable);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetTexture(Uri uri, bool nonReadable);

### Parameters

uri | The URI of the image to download.  
---|---  
nonReadable | If true, the texture's raw data will not be accessible to script. This can conserve memory. Default: `false`.  
  
### Returns

**UnityWebRequest** A [UnityWebRequest](Networking.UnityWebRequest.html)
properly configured to download an image and convert it to a
[Texture](Texture.html).

### Description

Create a [UnityWebRequest](Networking.UnityWebRequest.html) intended to
download an image via HTTP GET and create a [Texture](Texture.html) based on
the retrieved data.

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
  
Please note that the texture will be created as if it stores color data
(Additional resources: [TextureImporter.sRGBTexture](TextureImporter-
sRGBTexture.html)).  
  
**Note:** Only JPG and PNG formats are supported.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class MyBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(GetText());
        }  
      
        IEnumerator GetText()
        {
            using ([UnityWebRequest](Networking.UnityWebRequest.html) uwr = [UnityWebRequestTexture.GetTexture](Networking.UnityWebRequestTexture.GetTexture.html)("https://www.my-server.com/myimage.png"))
            {
                yield return uwr.SendWebRequest();  
      
                if (uwr.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
                {
                    [Debug.Log](Debug.Log.html)(uwr.error);
                }
                else
                {
                    // Get downloaded asset bundle
                    var texture = [DownloadHandlerTexture.GetContent](Networking.DownloadHandlerTexture.GetContent.html)(uwr);
                }
            }
        }
    }
    

* * *

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetTexture(string uri,
[Networking.DownloadedTextureParams](Networking.DownloadedTextureParams.html)
parameters);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetTexture(Uri uri,
[Networking.DownloadedTextureParams](Networking.DownloadedTextureParams.html)
parameters);

### Parameters

uri | The URI of the image to download.  
---|---  
parameters | Parameters specifying various properties of texture that will be created.  
  
### Returns

**UnityWebRequest** A [UnityWebRequest](Networking.UnityWebRequest.html)
properly configured to download an image and convert it to a
[Texture](Texture.html).

### Description

Create a [UnityWebRequest](Networking.UnityWebRequest.html) intended to
download an image via HTTP GET and create a [Texture](Texture.html) based on
the retrieved data.

Same as an overload with only `uri` parameter, except that it allows more
control over the properties of texture that will be created. For example,
using this overload you can disable creation of mipmaps or use linear color
space.

    
    
    using System.Collections;
    using UnityEngine;
    using UnityEngine.Networking;  
      
    public class NewMonoBehaviourScript : [MonoBehaviour](MonoBehaviour.html)
    {
       void Start()
       {
           StartCoroutine(GetText());
       }  
      
        IEnumerator GetText()
        {
            // Use linear color space and reduce memory usage by disabling mipmaps and ability to read pixels
            var parameters = [DownloadedTextureParams.Default](Networking.DownloadedTextureParams.Default.html);
            parameters.readable = false;
            parameters.mipmapChain = false;
            parameters.linearColorSpace = true;
            using ([UnityWebRequest](Networking.UnityWebRequest.html) uwr = [UnityWebRequestTexture.GetTexture](Networking.UnityWebRequestTexture.GetTexture.html)("https://www.my-server.com/myimage.png", parameters))
            {
                yield return uwr.SendWebRequest();  
      
                if (uwr.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
                {
                    [Debug.Log](Debug.Log.html)(uwr.error);
                }
                else
                {
                    // Get downloaded asset bundle
                    var texture = [DownloadHandlerTexture.GetContent](Networking.DownloadHandlerTexture.GetContent.html)(uwr);
                }
            }
        } 
    }
    

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

