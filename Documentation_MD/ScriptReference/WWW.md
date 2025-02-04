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

# WWW

class in UnityEngine

/

Inherits from:[CustomYieldInstruction](CustomYieldInstruction.html)

/

Implemented
in:[UnityEngine.UnityWebRequestWWWModule](UnityEngine.UnityWebRequestWWWModule.html)

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

### Description

Simple access to web pages.

Obsolete: WWW has been replaced with
[UnityWebRequest](Networking.UnityWebRequest.html).  
  
This is a small utility module for retrieving the contents of URLs.  
  
You start a download in the background by calling `WWW(url)` which returns a
new WWW object.  
  
You can inspect the `isDone` property to see if the download has completed or
yield the download object to automatically wait until it is (without blocking
the rest of the game).  
  
Use it if you want to get some data from a web server for integration with a
game such as highscore lists or calling home for some reason. There is also
functionality to create textures from images downloaded from the web and to
stream & load new web player data files.  
  
The WWW class can be used to send both GET and POST requests to the server.
The WWW class will use GET by default and POST if you supply a postData
parameter.  
  
Additional resources: [WWWForm](WWWForm.html) for a way to build valid form
data for the postData parameter.  
  
**Note:** URLs passed to WWW class must be '%' escaped.  
  
**Notes** **http://** , **https://** and **file://** protocols are supported
on iPhone. **ftp://** protocol support is limited to anonymous downloads only.
Other protocols are not supported.  
  
**Note:** When using file protocol on Windows and Windows Store Apps for
accessing local files, you have to specify **file:///** (with three slashes).

    
    
    // Get the Unity logo as a texture from the Unity website
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public string url = "https://unity3d.com/files/images/ogimg.jpg";
        IEnumerator Start()
        {
            using (WWW www = new WWW(url))
            {
                yield return www;
                [Renderer](Renderer.html) renderer = GetComponent<[Renderer](Renderer.html)>();
                renderer.material.mainTexture = www.texture;
            }
        }
    }
    

### Inherited Members

### Properties

[keepWaiting](CustomYieldInstruction-keepWaiting.html)| Indicates if coroutine
should be kept suspended.  
---|---  
  
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

