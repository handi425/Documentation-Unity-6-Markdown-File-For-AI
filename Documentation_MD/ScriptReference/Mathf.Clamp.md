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

#  [Mathf](Mathf.html).Clamp

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

public static float Clamp(float value, float min, float max);

### Parameters

value | The floating point value to restrict inside the range defined by the minimum and maximum values.  
---|---  
min | The minimum floating point value to compare against.  
max | The maximum floating point value to compare against.  
  
### Returns

**float** The float result between the minimum and maximum values.

### Description

Clamps the given value between the given minimum float and maximum float
values. Returns the given value if it is within the minimum and maximum range.

Returns the minimum value if the given float value is less than the minimum.
Returns the maximum value if the given value is greater than the maximum
value. Use Clamp to restrict a value to a range that is defined by the minimum
and maximum values.  
Returns an undefined value if the minimum value is greater than the maximum
value.

    
    
    using UnityEngine;  
      
    // [Mathf.Clamp](Mathf.Clamp.html) example.
    //
    // Animate a cube along the x-axis using a sine wave.
    // Let the minimum and maximum positions on the x-axis
    // be changed.  The cube will be visible inside the
    // minimum and maximum values.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        private float xMin = -0.5f, xMax = 0.5f;
        private float timeValue = 0.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Compute the sin position.
            float xValue = [Mathf.Sin](Mathf.Sin.html)(timeValue * 5.0f);  
      
            // Now compute the Clamp value.
            float xPos = [Mathf.Clamp](Mathf.Clamp.html)(xValue, xMin, xMax);  
      
            // [Update](PlayerLoop.Update.html) the position of the cube.
            transform.position = new [Vector3](Vector3.html)(xPos, 0.0f, 0.0f);  
      
            // Increase animation time.
            timeValue = timeValue + [Time.deltaTime](Time-deltaTime.html);  
      
            // Reset the animation time if it is greater than the planned time.
            if (xValue > [Mathf.PI](Mathf.PI.html) * 2.0f)
            {
                timeValue = 0.0f;
            }
        }  
      
        void OnGUI()
        {
            // Let the minimum and maximum values be changed
            xMin = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 25, 100, 30), xMin, -1.0f, +1.0f);
            xMax = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 60, 100, 30), xMax, -1.0f, +1.0f);  
      
            // xMin is kept less-than or equal to xMax.
            if (xMin > xMax)
            {
                xMin = xMax;
            }  
      
            // [Display](Display.html) the xMin and xMax value with better size labels.
            [GUIStyle](GUIStyle.html) fontSize = new [GUIStyle](GUIStyle.html)(GUI.skin.GetStyle("label"));
            fontSize.fontSize = 24;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(135, 10, 150, 30), "xMin: " + xMin.ToString("f2"), fontSize);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(135, 45, 150, 30), "xMax: " + xMax.ToString("f2"), fontSize);
        }
    }
    

* * *

## Declaration

public static int Clamp(int value, int min, int max);

### Parameters

value | The integer point value to restrict inside the min-to-max range.  
---|---  
min | The minimum integer point value to compare against.  
max | The maximum integer point value to compare against.  
  
### Returns

**int** The int result between min and max values.

### Description

Clamps the given value between a range defined by the given minimum integer
and maximum integer values. Returns the given value if it is within min and
max.

Returns the min value if the given value is less than the min value. Returns
the max value if the given value is greater than the max value. The min and
max parameters are inclusive. For example, Clamp(10, 0, 5) will return a
maximum argument of 5 and not 4.

    
    
    using UnityEngine;  
      
    // [Mathf.Clamp](Mathf.Clamp.html) integer example.
    //
    // Add or subtract values from health.
    // Keep health between 1 and 100. Start at 17.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public int health = 17;
        private int[] healthUp = new int[] {25, 10, 5, 1};
        private int[] healthDown = new int[] {-10, -5, -2, -1};  
      
        // Width and height for the buttons.
        private int xButton = 75;
        private int yButton = 50;  
      
        // Place of the top left button.
        private int xPos1 = 50, yPos1 = 100;
        private int xPos2 = 125, yPos2 = 100;  
      
        void OnGUI()
        {
            GUI.skin.label.fontSize = 20;
            GUI.skin.button.fontSize = 20;  
      
            // Generate and show positive buttons.
            for (int i = 0; i < healthUp.Length; i++)
            {
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(xPos1, yPos1 + i * yButton, xButton, yButton), healthUp[i].ToString()))
                {
                    health += healthUp[i];
                }
            }  
      
            // Generate and show negative buttons.
            for (int i = 0; i < healthDown.Length; i++)
            {
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(xPos2, yPos2 + i * yButton, xButton, yButton), healthDown[i].ToString()))
                {
                    health += healthDown[i];
                }
            }  
      
            // Show health between 1 and 100.
            health = [Mathf.Clamp](Mathf.Clamp.html)(health, 1, 100);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(xPos1, xPos1, 2 * xButton, yButton), "Health: " + health.ToString("D3"));
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

