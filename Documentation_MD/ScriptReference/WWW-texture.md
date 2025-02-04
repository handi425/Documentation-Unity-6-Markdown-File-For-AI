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

**Method group is Obsolete**  

#  [WWW](WWW.html).texture

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

**Obsolete** Use UnityWebRequest, a fully featured replacement which is more
efficient and has additional features. public [Texture2D](Texture2D.html)
texture;

### Description

Returns a [Texture2D](Texture2D.html) generated from the downloaded data (Read
Only).

The data must be an image in JPG or PNG format. If the data is not a valid
image, the generated texture will be a small image of a question mark. It is
recommended to use power-of-two size for each dimension of the image;
arbitrary sizes will also work but can load slightly slower and take up a bit
more memory. Each invocation of texture property allocates a new
[Texture2D](Texture2D.html). If you continously download textures you must use
[LoadImageIntoTexture](WWW.LoadImageIntoTexture.html) or
[Destroy](Object.Destroy.html) the previously created texture.  
  
For PNG files, gamma correction is applied to the texture if PNG file contains
gamma information. Display gamma for correction is assumed to be 2.0. If file
does not contain gamma information, no color correction will be performed.  
  
JPG files are loaded into [RGB24](TextureFormat.RGB24.html) format, PNG files
are loaded into [ARGB32](TextureFormat.ARGB32.html) format. If you want to
DXT-compress the downloaded image, use
[LoadImageIntoTexture](WWW.LoadImageIntoTexture.html) instead.  
  
If the object has not finished downloading the data a dummy image will be
returned. Use isDone or [yield](YieldInstruction.html) to see if the data is
available.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Get the latest webcam shot from outside "Friday's" in Times Square
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public string url = "https://images.earthcam.com/ec_metros/ourcams/fridays.jpg";  
      
        IEnumerator Start()
        {
            // Start a download of the given URL
            using (WWW www = new WWW(url))
            {
                // Wait for download to complete
                yield return www;  
      
                // assign texture
                [Renderer](Renderer.html) renderer = GetComponent<[Renderer](Renderer.html)>();
                renderer.material.mainTexture = www.texture;
            }
        }
    }
    

**Note:** The WWW.texture property allocates a new [Texture2D](Texture2D.html)
every time it is called. Therefore, it is important to always assign the
result to a local variable so that it can later be freed using Destroy().  
  
The call to www.texture allocates a new texture, but the texture is never
deallocated because no local reference to it exists.  
  
Alternatively, use WWW.LoadImageIntoTexture.

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

