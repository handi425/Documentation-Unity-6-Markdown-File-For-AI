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

#  [Touch](Touch.html).phase

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

public [TouchPhase](TouchPhase.html) phase;

### Description

Describes the phase of the touch.

The touch `phase` refers to the action the finger has taken on the most recent
frame update. Since a touch is tracked over its "lifetime" by the device, the
start and end of a touch and movements in between can be reported on the
frames they occur. The `phase` property can be used as the basis of a "switch'
statement or as part of a more sophisticated state handling system.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector2](Vector2.html) startPos;
        public [Vector2](Vector2.html) direction;
        public bool directionChosen;
        void [Update](PlayerLoop.Update.html)()
        {
            // Track a single touch as a direction control.
            if ([Input.touchCount](Input-touchCount.html) > 0)
            {
                [Touch](Touch.html) touch = [Input.GetTouch](Input.GetTouch.html)(0);  
      
                // Handle finger movements based on touch phase.
                switch (touch.phase)
                {
                    // Record initial touch position.
                    case [TouchPhase.Began](TouchPhase.Began.html):
                        startPos = touch.position;
                        directionChosen = false;
                        break;  
      
                    // Determine direction by comparing the current touch position with the initial one.
                    case [TouchPhase.Moved](TouchPhase.Moved.html):
                        direction = touch.position - startPos;
                        break;  
      
                    // Report that a direction has been chosen when the finger is lifted.
                    case [TouchPhase.Ended](TouchPhase.Ended.html):
                        directionChosen = true;
                        break;
                }
            }
            if (directionChosen)
            {
                // Something that uses the chosen direction...
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

