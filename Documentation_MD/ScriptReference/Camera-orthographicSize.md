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

#  [Camera](Camera.html).orthographicSize

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

public float orthographicSize;

### Description

Camera's half-size when in orthographic mode.

The `orthographicSize` property defines the viewing volume of an
[orthographic](Camera-orthographic.html) Camera. To edit `orthographicSize`,
you must set the Camera projection to orthographic.  
  
The height of the viewing volume is (`orthographicSize` * 2). Unity calculates
the width of the viewing volume using `orthographicSize` and the camera's
[aspect](Camera-aspect.html).  
  
Unity ignores `orthographicSize` if the camera is not orthographic. Use
[fieldOfView](Camera-fieldOfView.html) instead.  
  
Additional resources: [camera component](../Manual/class-Camera.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //Assign this [Camera](Camera.html) in the Inspector
        public [Camera](Camera.html) m_OrthographicCamera;
        //These are the positions and dimensions of the [Camera](Camera.html) view in the Game view
        float m_ViewPositionX, m_ViewPositionY, m_ViewWidth, m_ViewHeight;  
      
        void Start()
        {
            // This sets the [Camera](Camera.html) view rectangle to be in the bottom corner of the screen
            m_ViewPositionX = 0;
            m_ViewPositionY = 0;  
      
            // This sets the [Camera](Camera.html) view rectangle to be smaller so you can compare the orthographic view of this [Camera](Camera.html) with the perspective view of the Main [Camera](Camera.html)
            m_ViewWidth = 0.4f;
            m_ViewHeight = 0.4f;  
      
            // This enables the [Camera](Camera.html) (the one that is orthographic)
            m_OrthographicCamera.enabled = true;  
      
            // If the [Camera](Camera.html) exists in the inspector, enable orthographic mode and change the size
            if (m_OrthographicCamera)
            {
                // This enables the orthographic mode
                m_OrthographicCamera.orthographic = true;  
      
                // Set the size of the viewing volume you'd like the orthographic [Camera](Camera.html) to pick up
                m_OrthographicCamera.orthographicSize = 5.0f;  
      
                // Set the orthographic [Camera](Camera.html) Viewport size and position
                m_OrthographicCamera.rect = new [Rect](Rect.html)(m_ViewPositionX, m_ViewPositionY, m_ViewWidth, m_ViewHeight);
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

