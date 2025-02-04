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

# ForceMode2D

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

Option for how to apply a force using
[Rigidbody2D.AddForce](Rigidbody2D.AddForce.html).

Use this to apply a certain type of force to a 2D RigidBody. There are two
types of forces to apply: Force mode and Impulse Mode. For a 3D Rigidbody see
[ForceMode](ForceMode.html).

    
    
    //This script adds force to a [Rigidbody](Rigidbody.html). The kind of force is determined by which buttons you click.  
      
    //Create a [Sprite](Sprite.html) and attach a [Rigidbody2D](Rigidbody2D.html) component to it
    //Attach this script to the [Sprite](Sprite.html)  
      
    using UnityEngine;
    using UnityEngine.EventSystems;  
      
    public class AddingForce : [MonoBehaviour](MonoBehaviour.html)
    {
        //Use to switch between Force Modes
        enum ModeSwitching { Start, Impulse, Force };
        ModeSwitching m_ModeSwitching;  
      
        //Use this to change the different kinds of force
        [ForceMode2D](ForceMode2D.html) m_ForceMode;
        //Start position of the RigidBody, use to reset
        [Vector2](Vector2.html) m_StartPosition;  
      
        //Use to apply force to RigidBody
        [Vector2](Vector2.html) m_NewForce;  
      
        //Use to manipulate the RigidBody of a [GameObject](GameObject.html)
        [Rigidbody2D](Rigidbody2D.html) m_Rigidbody;  
      
        void Start()
        {
            //Fetch the RigidBody component attached to the [GameObject](GameObject.html)
            m_Rigidbody = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();
            //Start at first mode (nothing happening yet)
            m_ModeSwitching = ModeSwitching.Start;  
      
            //Initialising the force to use on the RigidBody in various ways
            m_NewForce = new [Vector2](Vector2.html)(-5.0f, 1.0f);  
      
            //This is the RigidBody's starting position
            m_StartPosition = m_Rigidbody.transform.position;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Switching modes depending on button presses
            switch (m_ModeSwitching)
            {
                //This is the starting mode which resets the [GameObject](GameObject.html)
                case ModeSwitching.Start:  
      
                    //Reset to starting position of RigidBody
                    m_Rigidbody.transform.position = m_StartPosition;
                    //Reset the velocity of the RigidBody
                    m_Rigidbody.velocity = new [Vector2](Vector2.html)(0f, 0f);
                    break;  
      
                //This is the Force [Mode](Scripting.GarbageCollector.Mode.html)
                case ModeSwitching.Force:
                    //Make the [GameObject](GameObject.html) travel upwards
                    m_NewForce = new [Vector2](Vector2.html)(0, 1.0f);
                    //Use Force mode as force on the RigidBody
                    m_Rigidbody.AddForce(m_NewForce, [ForceMode2D.Force](ForceMode2D.Force.html));
                    break;  
      
                //This is the Impulse [Mode](Scripting.GarbageCollector.Mode.html)
                case ModeSwitching.Impulse:
                    //Make the [GameObject](GameObject.html) travel upwards
                    m_NewForce = new [Vector2](Vector2.html)(0f, 1.0f);
                    //Use Impulse mode as a force on the RigidBody
                    m_Rigidbody.AddForce(m_NewForce, [ForceMode2D.Impulse](ForceMode2D.Impulse.html));
                    break;
            }
        }  
      
        //These are the Buttons for telling what Force to apply as well as resetting
        void OnGUI()
        {
            //If reset button pressed
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(100, 0, 150, 30), "Reset"))
            {
                //[Switch](PlayerSettings.Switch.html) to start/reset case  
      
                m_ModeSwitching = ModeSwitching.Start;
            }  
      
            //Impulse button pressed
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(100, 60, 150, 30), "Apply Impulse"))
            {
                //[Switch](PlayerSettings.Switch.html) to Impulse mode (apply impulse forces to [GameObject](GameObject.html))  
      
                m_ModeSwitching = ModeSwitching.Impulse;
            }  
      
            //Force [Button](UIElements.Button.html) Pressed
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(100, 90, 150, 30), "Apply Force"))
            {
                //[Switch](PlayerSettings.Switch.html) to Force mode (apply force to [GameObject](GameObject.html))
                m_ModeSwitching = ModeSwitching.Force;
            }
        }
    }
    

### Properties

[Force](ForceMode2D.Force.html)| Add a force to the Rigidbody2D, using its
mass.  
---|---  
[Impulse](ForceMode2D.Impulse.html)| Add an instant force impulse to the
rigidbody2D, using its mass.  
  
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

