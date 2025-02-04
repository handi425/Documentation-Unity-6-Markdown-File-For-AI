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

#  [Camera](Camera.html).fieldOfView

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

public float fieldOfView;

### Description

The vertical field of view of the Camera, in degrees.

This is the vertical field of view; horizontal field of view depends on the
viewport's aspect ratio. For for more information, see
[VerticalToHorizontalFieldOfView](Camera.VerticalToHorizontalFieldOfView.html).  
  
If [Camera.orthographic](Camera-orthographic.html) is `true`, the Camera
ignores `fieldOfView`.  
  
Some VR SDKs have fixed field of view values that are used for VR cameras.
When VR is enabled with those SDKs, this property will always return the value
from the SDK. You will see a warning logged if you attempt to set the property
and the value will be ignored.  
  
If you make changes to [Camera.projectionMatrix](Camera-
projectionMatrix.html), the Camera ignores `fieldOfView`. This lasts until you
call [Camera.ResetProjectionMatrix](Camera.ResetProjectionMatrix.html).  
  
In the Unity Editor, this corresponds to the **Clipping Planes: Near**
property in the Camera component Inspector.  
  
Additional resources: [Camera Inspector reference](../Manual/class-
Camera.html).

    
    
    //Attach this script to an empty [GameObject](GameObject.html).
    //This script creates a [Slider](UIElements.Slider.html) that allows you to manipulate the [Camera](Camera.html)'s field of view. Place GameObjects in the [Scene](SceneManagement.Scene.html) to show the full effect.  
      
    using UnityEngine;  
      
    public class CameraFieldOfViewExample : [MonoBehaviour](MonoBehaviour.html)
    {
        //This is the field of view that the [Camera](Camera.html) has
        float m_FieldOfView;  
      
        void Start()
        {
            //Start the [Camera](Camera.html) field of view at 60
            m_FieldOfView = 60.0f;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //[Update](PlayerLoop.Update.html) the camera's field of view to be the variable returning from the [Slider](UIElements.Slider.html)
            Camera.main.fieldOfView = m_FieldOfView;
        }  
      
        void OnGUI()
        {
            //Set up the maximum and minimum values the [Slider](UIElements.Slider.html) can return (you can change these)
            float max, min;
            max = 150.0f;
            min = 20.0f;
            //This [Slider](UIElements.Slider.html) changes the field of view of the [Camera](Camera.html) between the minimum and maximum values
            m_FieldOfView = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(20, 20, 100, 40), m_FieldOfView, min, max);
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

