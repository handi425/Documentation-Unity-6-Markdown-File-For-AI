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

#  [Camera](Camera.html).pixelRect

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

public [Rect](Rect.html) pixelRect;

### Description

Where on the screen is the camera rendered in pixel coordinates.

    
    
    //Attach this script to an empty [GameObject](GameObject.html)
    //Create a new [Camera](Camera.html) (**Create** >**Camera**) and position it appropriately. Attach it to the Second [Camera](Camera.html) field in the Inspector of the [GameObject](GameObject.html)
    //Press the space key to enable and disable the second [Camera](Camera.html)  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //Attach a new [Camera](Camera.html) in the Inspector window
        public [Camera](Camera.html) m_SecondCamera;
        //This is set as the main [Camera](Camera.html) in this script
        [Camera](Camera.html) m_FirstCamera;  
      
        void Start()
        {
            //Disable the second [Camera](Camera.html)
            m_SecondCamera.enabled = false;
            //Set where to place the second [Camera](Camera.html) along with its width and height
            m_SecondCamera.pixelRect = new [Rect](Rect.html)(0, 0, 400, 200);
            //Set the first [Camera](Camera.html) as the main [Camera](Camera.html)
            m_FirstCamera = [Camera.main](Camera-main.html);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the space key to toggle the second [Camera](Camera.html) and output camera pixel width and height
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                //Check if the second camera is enabled yet
                if (!m_SecondCamera.enabled)
                {
                    //[Toggle](UIElements.Toggle.html) the second [Camera](Camera.html) and output the second [Camera](Camera.html)'s details
                    ToggleCamera(m_SecondCamera, m_SecondCamera);
                }
                else
                {
                    //[Toggle](UIElements.Toggle.html) the second [Camera](Camera.html) and output the first [Camera](Camera.html)'s details
                    ToggleCamera(m_SecondCamera, m_FirstCamera);
                }
            }
        }  
      
        //[Toggle](UIElements.Toggle.html) the [Camera](Camera.html) and output the [Camera](Camera.html) specified
        void ToggleCamera([Camera](Camera.html) cameraToggle, [Camera](Camera.html) cameraOutput)
        {
            //Set [Camera](Camera.html) on and off
            cameraToggle.enabled = !cameraToggle.enabled;  
      
            //Output the [Camera](Camera.html)'s new Pixel width
            [Debug.Log](Debug.Log.html)("Pixel width :" + cameraOutput.pixelWidth + " Pixel height : " + cameraOutput.pixelHeight);
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

