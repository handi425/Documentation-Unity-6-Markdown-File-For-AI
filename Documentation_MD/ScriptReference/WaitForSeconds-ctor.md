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

# WaitForSeconds Constructor

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

## Declaration

public WaitForSeconds(float seconds);

### Parameters

seconds | Delay execution by the amount of time in seconds.  
---|---  
  
### Description

Suspends the coroutine execution for the given amount of seconds using scaled
time.

Create a `yield` instruction. Wait for `seconds` multiplied by
[Time.scaledTime](Time-scaledTime.html). If `seconds` is set to `2.0f` and
[Time.scaledTime](Time-scaledTime.html) is set to `0.5f`, the wait is `4.0f`
(`2.0f` divided by `0.5f` seconds). The example
[WaitForSeconds](WaitForSeconds.html) has a value of `1.0f`. The second button
changes [Time.scaledTime](Time-scaledTime.html) to `4.0f`. The cubes now move
faster.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // [WaitForSeconds](WaitForSeconds.html) example.
    //
    // Create three cubes. Press the "Move cubes normally" button to animate them.
    // Press the "Move cubes quickly" button to animate them faster.
    // Have [WaitForSeconds](WaitForSeconds.html) wait for different amounts of time. The cubes
    // move upward or downward one at a time.  
      
    public class ScriptExample : [MonoBehaviour](MonoBehaviour.html)
    {
        private [GameObject](GameObject.html)[] gameObjects;
        private int numberOfGameObjects = 3;
        private bool exampleInUse = false;
        private int width, height;
        private float xPos, yPos;
        private float xSize, ySize;
        private int fontSize;  
      
        void Awake()
        {
            gameObjects = new [GameObject](GameObject.html)[numberOfGameObjects];  
      
            for (int i = 0; i < numberOfGameObjects; i++)
            {
                // Create a cube, place in the world, and set the name.
                gameObjects[i] = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
                gameObjects[i].transform.position = new [Vector3](Vector3.html)(-1.5f + i * 1.5f, 0.5f, 0.0f);
                gameObjects[i].name = i.ToString();
            }  
      
            // The size and position of the buttons.
            width = [Screen.width](Screen-width.html);
            height = [Screen.height](Screen-height.html);
            xPos = width - width / 2.5f;
            yPos = height - height / 5;
            xSize = 250 * width / 800;
            ySize = 40 * height / 600;
            fontSize = 24 * width / 800;  
      
            // Place the camera in a good location and looking towards the cubes.
            Camera.main.transform.position = new [Vector3](Vector3.html)(2.6f, 2.0f, 2.5f);
            Camera.main.transform.localEulerAngles = new [Vector3](Vector3.html)(25.0f, -135.0f, 0.0f);
        }  
      
        // Move selected cube up or down.
        void ChangeSize(int gameObject, float x)
        {
            if (gameObjects[gameObject].transform.position.y > 0.95f)
            {
                gameObjects[gameObject].transform.position = new [Vector3](Vector3.html)(x, 0.5f, 0.0f);
            }
            else
            {
                gameObjects[gameObject].transform.position = new [Vector3](Vector3.html)(x, 1.0f, 0.0f);
            }
        }  
      
        IEnumerator Example()
        {
            // Start control of the three cubes.
            exampleInUse = true;  
      
            // Move the first cube up or down.
            yield return new [WaitForSeconds](WaitForSeconds.html)(0.5f);
            ChangeSize(0, -1.5f);  
      
            // Move the second cube up or down.
            yield return new [WaitForSeconds](WaitForSeconds.html)(1.5f);
            ChangeSize(1, 0.0f);  
      
            // Move the third cube up or down.
            yield return new [WaitForSeconds](WaitForSeconds.html)(0.75f);
            ChangeSize(2, 1.5f);  
      
            // Pause for a second.
            yield return new [WaitForSeconds](WaitForSeconds.html)(1.0f);  
      
            exampleInUse = false;
        }  
      
        void OnGUI()
        {
            [GUI.enabled](GUI-enabled.html) = !exampleInUse;
            GUI.skin.button.fontSize = 24 * width / 800;  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(xPos, yPos, xSize, ySize), "Move cubes normally"))
            {
                [Time.timeScale](Time-timeScale.html) = 1.0f;
                StartCoroutine(Example());
            }  
      
            // Set the speed of the cubes to be more fast than normal.
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(xPos, yPos + ySize * 1.1f, xSize, ySize), "Move cubes quickly"))
            {
                [Time.timeScale](Time-timeScale.html) = 4.0f;
                StartCoroutine(Example());
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

