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

#  [MonoBehaviour](MonoBehaviour.html).Update()

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Description

Update is called every frame, if the MonoBehaviour is enabled.

`Update` is the most commonly used function to implement any kind of game
script. Not every `MonoBehaviour` script needs `Update`.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // The ExampleClass starts with Awake.  The [GameObject](GameObject.html) class has activeSelf
    // set to false.  When activeSelf is set to true the Start() and [Update](PlayerLoop.Update.html)()
    // functions will be called causing the ExampleClass to run.
    // Note that ExampleClass (Script) in the Inspector is turned off.  It
    // needs to be ticked to make script call Start.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private float update;  
      
        void Awake()
        {
            [Debug.Log](Debug.Log.html)("Awake");
            update = 0.0f;
        }  
      
        IEnumerator Start()
        {
            [Debug.Log](Debug.Log.html)("Start1");
            yield return new [WaitForSeconds](WaitForSeconds.html)(2.5f);
            [Debug.Log](Debug.Log.html)("Start2");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            update += [Time.deltaTime](Time-deltaTime.html);
            if (update > 1.0f)
            {
                update = 0.0f;
                [Debug.Log](Debug.Log.html)("[Update](PlayerLoop.Update.html)");
            }
        }
    }
    

In order to get the elapsed time since last call to Update, use
[Time.deltaTime](Time-deltaTime.html). This function is only called if the
[Behaviour](Behaviour.html) is enabled. Override this function in order to
provide your component's functionality.

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

