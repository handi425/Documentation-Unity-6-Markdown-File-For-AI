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

#  [Light](Light.html).color

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

[Switch to Manual](../Manual/class-Light.html "Go to Light Component in the
Manual")

public [Color](Color.html) color;

### Description

The color of the light.

To modify the light intensity you change light's color luminance. Lights
always add illumination, so a light with a black color is the same as no light
at all. Additional resources: [Light component](../Manual/class-Light.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Light](Light.html) lt;  
      
        void Start()
        {
            lt = GetComponent<[Light](Light.html)>();
        }  
      
        // Darken the light completely over a period of 2 seconds.
        void [Update](PlayerLoop.Update.html)()
        {
            lt.color -= ([Color.white](Color-white.html) / 2.0f) * [Time.deltaTime](Time-deltaTime.html);
        }
    }
    

Another example:

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Interpolate light color between two colors back and forth
        float duration = 1.0f;
        [Color](Color.html) color0 = [Color.red](Color-red.html);
        [Color](Color.html) color1 = [Color.blue](Color-blue.html);  
      
        [Light](Light.html) lt;  
      
        void Start()
        {
            lt = GetComponent<[Light](Light.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // set light color
            float t = [Mathf.PingPong](Mathf.PingPong.html)([Time.time](Time-time.html), duration) / duration;
            lt.color = [Color.Lerp](Color.Lerp.html)(color0, color1, t);
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

