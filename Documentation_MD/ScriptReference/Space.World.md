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

#  [Space](Space.html).World

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

World coordinate space, relative to the origin point (0,0,0) of the x-, y-,
and z-axes of the scene.

Use `Space.World` to transform a GameObject relative to its
[Transform.position](Transform-position.html) and the scene axes, ignoring the
GameObject's own orientation. For example,
`Transform.Translate(Vector3.forward, Space.World)` adds one unit to the
object's [Transform.position](Transform-position.html) on the z-axis of the
scene.  
  
To transform a GameObject relative to its [Transform.localPosition](Transform-
localPosition.html) and along the object's own axes, use
[Space.Self](Space.Self.html).

    
    
    //Attach this script to a [GameObject](GameObject.html).
    //This example demonstrates the difference between [Space.World](Space.World.html) and [Space.Self](Space.Self.html) in rotation.
    //The m_WorldSpace field will be automatically exposed as a checkbox in the Inspector window labelled World [Space](Space.html). Enable or disable the checkbox in the Inspector to start in world or self respectively.
    //Press play to see the [GameObject](GameObject.html) rotating appropriately. Press space or toggle the World [Space](Space.html) checkbox to switch between World and Self.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        float m_Speed;
        public bool m_WorldSpace;  
      
        void Start()
        {
            //Set the speed of the rotation
            m_Speed = 20.0f;
            //[Rotate](UIElements.Rotate.html) the [GameObject](GameObject.html) a little at the start to show the difference between [Space](Space.html) and Local
            transform.Rotate(60, 0, 60);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //[Rotate](UIElements.Rotate.html) the [GameObject](GameObject.html) in World [Space](Space.html) if in the m_WorldSpace state
            if (m_WorldSpace)
                transform.Rotate([Vector3.up](Vector3-up.html) * m_Speed * [Time.deltaTime](Time-deltaTime.html), [Space.World](Space.World.html));
            //Otherwise, rotate the [GameObject](GameObject.html) in local space
            else
                transform.Rotate([Vector3.up](Vector3-up.html) * m_Speed * [Time.deltaTime](Time-deltaTime.html), [Space.Self](Space.Self.html));  
      
            //Press the [Space](Space.html) button to switch between world and local space states
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                //Make the current state switch to the other state
                m_WorldSpace = !m_WorldSpace;
                //Output the Current state to the console
                [Debug.Log](Debug.Log.html)("World [Space](Space.html) : " + m_WorldSpace.ToString());
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

