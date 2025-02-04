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

#  [Debug](Debug.html).Log

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

[Switch to Manual](../Manual/class-Debug.html "Go to Debug Component in the
Manual")

## Declaration

public static void Log(object message);

## Declaration

public static void Log(object message, [Object](Object.html) context);

### Parameters

message | String or object to be converted to string representation for display.  
---|---  
context | Object to which the message applies.  
  
### Description

Logs a message to the Unity Console.

Use [Debug.Log](Debug.Log.html) to print informational messages that help you
debug your application. For example, you could print a message containing a
[GameObject.name](GameObject-name.html) and information about the object’s
current state.  
  
You can format messages with string concatenation:  
`Debug.Log("Text: " + myText.text);`  
  
You can also use [Rich Text](../Manual/StyledText.html) markup.  
  
If you pass a [GameObject](GameObject.html) or [Component](Component.html) as
the optional `context` parameter, Unity momentarily highlights that object in
the `Hierarchy` window when you click the log message in the `Console`. Use a
`context` object when you have many instances of an object in a Scene so that
you can identify which one produced the message. `Example 2`, below,
illustrates how this feature works. When you run this example, first click one
of the cubes it creates in the Scene. The example prints a log message to the
`Console`. When you click on the message, Unity highlights the `context`
object in the `Hierarchy` window — in this case, the cube you clicked on in
the Scene.  
  
Example 1: Show some uses of [Debug.Log](Debug.Log.html):

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class MyGameClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // A [Light](Light.html) used in the [Scene](SceneManagement.Scene.html) and needed by MyGameMethod().
        public [Light](Light.html) light;  
      
        void MyGameMethod()
        {
            // [Message](VersionControl.Message.html) with a [GameObject](GameObject.html) name.
            [Debug.Log](Debug.Log.html)("Hello: " + gameObject.name);  
      
            // [Message](VersionControl.Message.html) with light type. This is an Object example.
            [Debug.Log](Debug.Log.html)(light.type);  
      
            // [Message](VersionControl.Message.html) using rich text.
            [Debug.Log](Debug.Log.html)("<color=red>[Error](PackageManager.Error.html): </color>[AssetBundle](AssetBundle.html) not found");
        }
    }
    

Example 2: Show selection of a clicked [GameObject](GameObject.html):

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // [Debug.Log](Debug.Log.html) example
    //
    // Create three cubes. Place them around the world origin.
    // If a cube is clicked use [Debug.Log](Debug.Log.html) to announce it. Use
    // [Debug.Log](Debug.Log.html) with two arguments. Argument two allows the
    // cube to be automatically selected in the hierarchy when
    // the console message is clicked.
    //
    // Add this script to an empty [GameObject](GameObject.html).  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private [GameObject](GameObject.html)[] cubes;  
      
        void Awake()
        {
            // Create three cubes and place them close to the world space center.
            cubes = new [GameObject](GameObject.html)[3];
            float f = 25.0f;
            float p = -2.0f;
            float[] z = new float[] {0.5f, 0.0f, 0.5f};  
      
            for (int i = 0; i < 3; i++)
            {
                // [Position](UIElements.Position.html) and rotate each cube.
                cubes[i] = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
                cubes[i].name = "Cube" + (i + 1).ToString();
                cubes[i].transform.Rotate(0.0f, f, 0.0f);
                cubes[i].transform.position = new [Vector3](Vector3.html)(p, 0.0f, z[i]);
                f -= 25.0f;
                p = p + 2.0f;
            }  
      
            // [Position](UIElements.Position.html) and rotate the camera to view all three cubes.
            Camera.main.transform.position = new [Vector3](Vector3.html)(3.0f, 1.5f, 3.0f);
            Camera.main.transform.localEulerAngles = new [Vector3](Vector3.html)(25.0f, -140.0f, 0.0f);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Process a mouse button click.
            if ([Input.GetMouseButtonDown](Input.GetMouseButtonDown.html)(0))
            {
                var ray = Camera.main.ScreenPointToRay([Input.mousePosition](Input-mousePosition.html));
                [RaycastHit](RaycastHit.html) hit;  
      
                if ([Physics.Raycast](Physics.Raycast.html)(ray, out hit))
                {
                    // Visit each cube and determine if it has been clicked.
                    for (int i = 0; i < 3; i++)
                    {
                        if (hit.collider.gameObject == cubes[i])
                        {
                            // This cube was clicked.
                            [Debug.Log](Debug.Log.html)("Hit " + cubes[i].name, cubes[i]);
                        }
                    }
                }
            }
        }
    }
    

Note: Unity also adds [Debug.Log](Debug.Log.html) messages to the Editor and
Player log files. See [Log Files](../Manual/LogFiles.html) for more
information about accessing these files on different platforms.  
  
Additional resources: [MonoBehaviour.print](MonoBehaviour-print.html).

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

