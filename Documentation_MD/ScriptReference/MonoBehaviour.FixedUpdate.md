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

#  [MonoBehaviour](MonoBehaviour.html).FixedUpdate()

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

Frame-rate independent
[MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html) message for
physics calculations.

[MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html) has the frequency
of the physics system; it is called every fixed frame-rate frame. Compute
[Physics](Physics.html) system calculations after
[FixedUpdate](MonoBehaviour.FixedUpdate.html). 0.02 seconds (50 calls per
second) is the default time between calls. Use [Time.fixedDeltaTime](Time-
fixedDeltaTime.html) to access this value. Alter it by setting it to your
preferred value within a script, or, navigate to `Edit > Settings > Time >
Fixed Timestep` and set it there. The
[FixedUpdate](MonoBehaviour.FixedUpdate.html) frequency is more or less than
[Update](MonoBehaviour.Update.html). If the application runs at 25 frames per
second (fps), Unity calls it approximately twice per frame, Alternatively, 100
fps causes approximately two rendering frames with one
[FixedUpdate](MonoBehaviour.FixedUpdate.html). Control the required frame rate
and `Fixed Timestep` rate from `Time` settings. Use
[Application.targetFrameRate](Application-targetFrameRate.html) to set the
frame rate.  
  
Use [FixedUpdate](MonoBehaviour.FixedUpdate.html) when using
[Rigidbody](Rigidbody.html). Set a force to a [Rigidbody](Rigidbody.html) and
it applies each fixed frame. [FixedUpdate](MonoBehaviour.FixedUpdate.html)
occurs at a measured time step that typically does not coincide with
[MonoBehaviour.Update](MonoBehaviour.Update.html).  
  
In the following example, the number of [Update](MonoBehaviour.Update.html)
calls is compared against the number of
[FixedUpdate](MonoBehaviour.FixedUpdate.html) calls.
[FixedUpdate](MonoBehaviour.FixedUpdate.html) executes 50 times per second.
(The game code runs around 200 fps on a test machine.)

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // GameObject.FixedUpdate example.
    //
    // Measure frame rate comparing [FixedUpdate](PlayerLoop.FixedUpdate.html) against [Update](PlayerLoop.Update.html).
    // Show the rates every second.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        private float updateCount = 0;
        private float fixedUpdateCount = 0;
        private float updateUpdateCountPerSecond;
        private float updateFixedUpdateCountPerSecond;  
      
        void Awake()
        {
            // Uncommenting this will cause framerate to drop to 10 frames per second.
            // This will mean that [FixedUpdate](PlayerLoop.FixedUpdate.html) is called more often than [Update](PlayerLoop.Update.html).
            //[Application.targetFrameRate](Application-targetFrameRate.html) = 10;
            StartCoroutine(Loop());
        }  
      
        // Increase the number of calls to [Update](PlayerLoop.Update.html).
        void [Update](PlayerLoop.Update.html)()
        {
            updateCount += 1;
        }  
      
        // Increase the number of calls to [FixedUpdate](PlayerLoop.FixedUpdate.html).
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            fixedUpdateCount += 1;
        }  
      
        // Show the number of calls to both messages.
        void OnGUI()
        {
            [GUIStyle](GUIStyle.html) fontSize = new [GUIStyle](GUIStyle.html)(GUI.skin.GetStyle("label"));
            fontSize.fontSize = 24;
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(100, 100, 200, 50), "[Update](PlayerLoop.Update.html): " + updateUpdateCountPerSecond.ToString(), fontSize);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(100, 150, 200, 50), "[FixedUpdate](PlayerLoop.FixedUpdate.html): " + updateFixedUpdateCountPerSecond.ToString(), fontSize);
        }  
      
        // [Update](PlayerLoop.Update.html) both CountsPerSecond values every second.
        IEnumerator Loop()
        {
            while (true)
            {
                yield return new [WaitForSeconds](WaitForSeconds.html)(1);
                updateUpdateCountPerSecond = updateCount;
                updateFixedUpdateCountPerSecond = fixedUpdateCount;  
      
                updateCount = 0;
                fixedUpdateCount = 0;
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

