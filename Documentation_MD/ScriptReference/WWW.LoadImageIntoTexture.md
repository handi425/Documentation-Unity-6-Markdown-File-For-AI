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

#  [WWW](WWW.html).LoadImageIntoTexture

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
efficient and has additional features.

## Declaration

public void LoadImageIntoTexture([Texture2D](Texture2D.html) texture);

### Parameters

tex | An existing texture object to be overwritten with the image data.  
---|---  
  
### Description

Replaces the contents of an existing [Texture2D](Texture2D.html) with an image
from the downloaded data.

The data must be an image in JPG or PNG format. If the data is not a valid
image, the generated texture will be a small image of a question mark. It is
recommended to use power-of-two size for each dimension of the image;
arbitrary sizes will also work but can load slightly slower and take up a bit
more memory.  
  
For PNG files, gamma correction is applied to the texture if PNG file contains
gamma information. Display gamma for correction is assumed to be 2.0. If file
does not contain gamma information, no color correction will be performed.  
  
This function replaces texture contents with downloaded image data, so texture
size and format might change. JPG files are loaded into
[RGB24](TextureFormat.RGB24.html) format, PNG files are loaded into
[ARGB32](TextureFormat.ARGB32.html) format. If texture format before calling
LoadImage is [DXT1](TextureFormat.DXT1.html) or
[DXT5](TextureFormat.DXT5.html), then the loaded image will be DXT-compressed
(into DXT1 for JPG images and DXT5 for PNG images).  
  
If the data has not finished downloading the texture will be left untouched.
Use isDone or `yield` to see if the data is available.

    
    
    // Add this script to a [GameObject](GameObject.html). The Start() function fetches an
    // image from the documentation site.  It is then applied as the
    // texture on the [GameObject](GameObject.html).  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public string url = "https://docs.unity3d.com/uploads/Main/ShadowIntro.png";  
      
        IEnumerator Start()
        {
            [Texture2D](Texture2D.html) tex;
            tex = new [Texture2D](Texture2D.html)(4, 4, [TextureFormat.DXT1](TextureFormat.DXT1.html), false);
            using (WWW www = new WWW(url))
            {
                yield return www;
                www.LoadImageIntoTexture(tex);
                GetComponent<[Renderer](Renderer.html)>().material.mainTexture = tex;
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

