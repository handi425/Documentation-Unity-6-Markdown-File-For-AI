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

# ForceMode

enumeration

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

### Description

Use ForceMode to specify how to apply a force using
[Rigidbody.AddForce](Rigidbody.AddForce.html) or
[ArticulationBody.AddForce](ArticulationBody.AddForce.html).

The AddForce function impacts how your GameObject moves by allowing you to
define your own force vector, as well as choosing how to apply this force to
the GameObject (this GameObject must have a Rigidbody component attached).  
  
ForceMode allows you to choose from four different ways to affect the
GameObject using this Force: Acceleration, Force, Impulse, and VelocityChange.  
  
For more information on how ForceMode affects velocity, see
[Rigidbody.AddForce](Rigidbody.AddForce.html).

    
    
    using UnityEngine;  
      
    public class ForceModeExample : [MonoBehaviour](MonoBehaviour.html)
    {
        //Use to switch between Force Modes
        enum ModeSwitching { Start, Impulse, Acceleration, Force, VelocityChange };
        ModeSwitching m_ModeSwitching;  
      
        [Vector3](Vector3.html) m_StartPos, m_StartForce;
        [Vector3](Vector3.html) m_NewForce;
        [Rigidbody](Rigidbody.html) m_Rigidbody;  
      
        string m_ForceXString = string.Empty;
        string m_ForceYString = string.Empty;  
      
        float m_ForceX, m_ForceY;
        float m_Result;  
      
        void Start()
        {
            //You get the [Rigidbody](Rigidbody.html) component you attach to the [GameObject](GameObject.html)
            m_Rigidbody = GetComponent<[Rigidbody](Rigidbody.html)>();  
      
            //This starts at first mode (nothing happening yet)
            m_ModeSwitching = ModeSwitching.Start;  
      
            //Initialising the force which is used on [GameObject](GameObject.html) in various ways
            m_NewForce = new [Vector3](Vector3.html)(-5.0f, 1.0f, 0.0f);  
      
            //Initialising floats
            m_ForceX = 0;
            m_ForceY = 0;  
      
            //The forces typed in from the text fields (the ones you can manipulate in Game view)
            m_ForceXString = "0";
            m_ForceYString = "0";  
      
            //The [GameObject](GameObject.html)'s starting position and [Rigidbody](Rigidbody.html) position
            m_StartPos = transform.position;
            m_StartForce = m_Rigidbody.transform.position;
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            //If the current mode is not the starting mode (or the [GameObject](GameObject.html) is not reset), the force can change
            if (m_ModeSwitching != ModeSwitching.Start)
            {
                //The force changes depending what you input into the text fields
                m_NewForce = new [Vector3](Vector3.html)(m_ForceX, m_ForceY, 0);
            }  
      
            //Here, switching modes depend on button presses in the Game mode
            switch (m_ModeSwitching)
            {
                //This is the starting mode which resets the [GameObject](GameObject.html)
                case ModeSwitching.Start:
                    //This resets the [GameObject](GameObject.html) and [Rigidbody](Rigidbody.html) to their starting positions
                    transform.position = m_StartPos;
                    m_Rigidbody.transform.position = m_StartForce;  
      
                    //This resets the velocity of the [Rigidbody](Rigidbody.html)
                    m_Rigidbody.velocity = new [Vector3](Vector3.html)(0f, 0f, 0f);
                    break;  
      
                //These are the modes [ForceMode](ForceMode.html) can force on a [Rigidbody](Rigidbody.html)
                //This is Acceleration mode
                case ModeSwitching.Acceleration:
                    //The function converts the text fields into floats and updates the [Rigidbody](Rigidbody.html)’s force
                    MakeCustomForce();  
      
                    //Use Acceleration as the force on the [Rigidbody](Rigidbody.html)
                    m_Rigidbody.AddForce(m_NewForce, [ForceMode.Acceleration](ForceMode.Acceleration.html));
                    break;  
      
                //This is Force [Mode](Scripting.GarbageCollector.Mode.html), using a continuous force on the [Rigidbody](Rigidbody.html) considering its mass
                case ModeSwitching.Force:
                    //Converts the text fields into floats and updates the force applied to the [Rigidbody](Rigidbody.html)
                    MakeCustomForce();  
      
                    //Use Force as the force on [GameObject](GameObject.html)’s [Rigidbody](Rigidbody.html)
                    m_Rigidbody.AddForce(m_NewForce, [ForceMode.Force](ForceMode.Force.html));
                    break;  
      
                //This is Impulse [Mode](Scripting.GarbageCollector.Mode.html), which involves using the [Rigidbody](Rigidbody.html)’s mass to apply an instant impulse force.
                case ModeSwitching.Impulse:
                    //The function converts the text fields into floats and updates the force applied to the [Rigidbody](Rigidbody.html)
                    MakeCustomForce();  
      
                    //Use Impulse as the force on [GameObject](GameObject.html)
                    m_Rigidbody.AddForce(m_NewForce, [ForceMode.Impulse](ForceMode.Impulse.html));
                    break;  
      
                //This is VelocityChange which involves ignoring the mass of the [GameObject](GameObject.html) and impacting it with a sudden speed change in a direction
                case ModeSwitching.VelocityChange:
                    //Converts the text fields into floats and updates the force applied to the [Rigidbody](Rigidbody.html)
                    MakeCustomForce();  
      
                    //Make a Velocity change on the [Rigidbody](Rigidbody.html)
                    m_Rigidbody.AddForce(m_NewForce, [ForceMode.VelocityChange](ForceMode.VelocityChange.html));
                    break;
            }
        }  
      
        //The function outputs buttons, text fields, and other interactable UI elements to the [Scene](SceneManagement.Scene.html) in Game view
        void OnGUI()
        {
            //Getting the inputs from each text field and storing them as strings
            m_ForceXString = [GUI.TextField](GUI.TextField.html)(new [Rect](Rect.html)(300, 10, 200, 20), m_ForceXString, 25);
            m_ForceYString = [GUI.TextField](GUI.TextField.html)(new [Rect](Rect.html)(300, 30, 200, 20), m_ForceYString, 25);  
      
            //Press the button to reset the [GameObject](GameObject.html) and [Rigidbody](Rigidbody.html)
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(100, 0, 150, 30), "Reset"))
            {
                //This switches to the start/reset case
                m_ModeSwitching = ModeSwitching.Start;
            }  
      
            //When you press the Acceleration button, switch to Acceleration mode
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(100, 30, 150, 30), "Apply Acceleration"))
            {
                //[Switch](PlayerSettings.Switch.html) to Acceleration (apply acceleration force to [GameObject](GameObject.html))
                m_ModeSwitching = ModeSwitching.Acceleration;
            }  
      
            //If you press the Impulse button
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(100, 60, 150, 30), "Apply Impulse"))
            {
                //[Switch](PlayerSettings.Switch.html) to impulse (apply impulse forces to [GameObject](GameObject.html))
                m_ModeSwitching = ModeSwitching.Impulse;
            }  
      
            //If you press the Force [Button](UIElements.Button.html), switch to Force state
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(100, 90, 150, 30), "Apply Force"))
            {
                //[Switch](PlayerSettings.Switch.html) to Force (apply force to [GameObject](GameObject.html))
                m_ModeSwitching = ModeSwitching.Force;
            }  
      
            //Press the button to switch to VelocityChange state
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(100, 120, 150, 30), "Apply Velocity Change"))
            {
                //[Switch](PlayerSettings.Switch.html) to velocity changing
                m_ModeSwitching = ModeSwitching.VelocityChange;
            }
        }  
      
        //Changing strings to floats for the forces
        float ConvertToFloat(string Name)
        {
            float.TryParse(Name, out m_Result);
            return m_Result;
        }  
      
        //Set the converted float from the text fields as the forces to apply to the [Rigidbody](Rigidbody.html)
        void MakeCustomForce()
        {
            //This converts the strings to floats
            m_ForceX = ConvertToFloat(m_ForceXString);
            m_ForceY = ConvertToFloat(m_ForceYString);
        }
    }
    

### Properties

[Force](ForceMode.Force.html)| Add a continuous force to the rigidbody, using
its mass.  
---|---  
[Acceleration](ForceMode.Acceleration.html)| Add a continuous acceleration to
the rigidbody, ignoring its mass.  
[Impulse](ForceMode.Impulse.html)| Add an instant force impulse to the
rigidbody, using its mass.  
[VelocityChange](ForceMode.VelocityChange.html)| Add an instant velocity
change to the rigidbody, ignoring its mass.  
  
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

