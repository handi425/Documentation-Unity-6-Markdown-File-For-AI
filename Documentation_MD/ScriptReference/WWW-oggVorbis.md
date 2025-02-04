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

#  [WWW](WWW.html).oggVorbis

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

**Obsolete** Obsolete msg.  
**Upgrade to[GetAudioClip](WWW-GetAudioClip.html)** public Object oggVorbis;

### Description

Load an Ogg Vorbis file into the audio clip.

If the stream has not been downloaded completely, null will be returned. Use
isDone or `yield` to see if the data is available.  
  
Additional resources: [AudioClip](AudioClip.html),
[AudioSource](AudioSource.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        string path = "http://ia301106.us.archive.org/2/items/abird2005-02-10/abird2005-02-10t02.ogg";  
      
        IEnumerator Start()
        {
            // Start downloading
            using (var download = new WWW(path))
            {
                // Wait for download to finish
                yield return download;
                // Create ogg vorbis file
                var clip = download.GetAudioClip();
                // Play it
                if (clip != null)
                {
                    GetComponent<[AudioSource](AudioSource.html)>().clip = clip;
                    GetComponent<[AudioSource](AudioSource.html)>().Play();
                }
                else     // Handle error
                {
                    [Debug.Log](Debug.Log.html)("Ogg vorbis download failed. (Incorrect link?)");
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

