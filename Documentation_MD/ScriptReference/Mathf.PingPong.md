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

#  [Mathf](Mathf.html).PingPong

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

[Switch to Manual](../Manual/class-Mathf.html "Go to Mathf Component in the
Manual")

## Declaration

public static float PingPong(float t, float length);

### Description

PingPong returns a value that increments and decrements between zero and the
length. It follows the triangle wave formula where the bottom is set to zero
and the peak is set to `length`.

PingPong requires the value `t` to be a self-incrementing value. For example,
Time.time and Time.unscaledTime.  
  
The example below shows a simple use case with the light intensity going from
0 to 8 to 0 continuously.

    
    
    using UnityEngine;  
      
    public class PingPongExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [Light](Light.html) myLight;  
      
        void Start()
        {
            myLight = GetComponent<[Light](Light.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            myLight.intensity = [Mathf.PingPong](Mathf.PingPong.html)([Time.time](Time-time.html), 8);
        }
    }
    

The example below shows some outputs as example.

    
    
    using UnityEngine;  
      
    public class OutputExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Prints 2
            [Debug.Log](Debug.Log.html)([Mathf.PingPong](Mathf.PingPong.html)(2, 5));  
      
            // Prints 3
            [Debug.Log](Debug.Log.html)([Mathf.PingPong](Mathf.PingPong.html)(7, 5));
     
            // Prints 1
            [Debug.Log](Debug.Log.html)([Mathf.PingPong](Mathf.PingPong.html)(11, 5));
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

