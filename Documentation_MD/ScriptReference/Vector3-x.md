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

#  [Vector3](Vector3.html).x

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

public float x;

### Description

X component of the vector.

Use this to modify or return the X component of a vector.

    
    
    // This script moves a [GameObject](GameObject.html) to a new x position using [Vector3.x](Vector3-x.html).
    // Attach this script to a [GameObject](GameObject.html)
    // Set your x position in the Inspector  
      
    using UnityEngine;  
      
    public class Examples : [MonoBehaviour](MonoBehaviour.html)
    {
        [Vector3](Vector3.html) m_NewPosition;
        // This is the new X position. Set it in the Inspector.
        public float m_XPosition;  
      
        // Use this for initialization
        void Start()
        {
            // Initialise the vector
            m_NewPosition = new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Press the space key to change the x component of the vector
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                m_NewPosition.x = m_XPosition;
            }
            // Change the position depending on the vector
            transform.position = m_NewPosition;
        }
    }
    

Below is another example that allows you to manipulate the GameObject’s x and
y positions. Just type an x and y position in the Input Fields in Play Mode.

    
    
    // Attach this script to a [GameObject](GameObject.html)
    // Create two [Input](Input.html) Fields in the [Scene](SceneManagement.Scene.html) (Create>UI>[Input](Input.html) Field)
    // Click on the [GameObject](GameObject.html) and attach both [Input](Input.html) Fields in the Inspector window  
      
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Vector3](Vector3.html) m_NewPosition;  
      
        // Attach these in the Inspector window
        public InputField m_InputFieldX, m_InputFieldY;  
      
        // These are the strings that are returned from the InputFields
        string xString, yString;  
      
        // These are used when converting the strings to floats
        float m_XValue, m_YValue;  
      
        // Use this for initialization
        void Start()
        {
            // Initialise the vector
            m_NewPosition = new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Store the inputs from the InputFields as strings
            xString = m_InputFieldX.text;
            yString = m_InputFieldY.text;  
      
            // Convert the strings from the InputFields to floats
            ConvertStringsToFloats(xString, yString);  
      
            // Change the NewPosition Vector's x and y components
            m_NewPosition.x = m_XValue;
            m_NewPosition.y = m_YValue;  
      
            // Change the position depending on the vector
            transform.position = m_NewPosition;
        }  
      
        void ConvertStringsToFloats(string XVal, string YVal)
        {
            try
            {
                // Convert the strings to floats
                m_XValue = float.Parse(XVal);
                m_YValue = float.Parse(YVal);
            }
            catch{}
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

