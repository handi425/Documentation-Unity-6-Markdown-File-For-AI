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

#  [GameObject](GameObject.html).activeInHierarchy

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

[Switch to Manual](../Manual/class-GameObject.html "Go to GameObject Component
in the Manual")

public bool activeInHierarchy;

### Description

The active state of the GameObject in the Scene hierarchy. True if active,
false if inactive. (Read Only)

A GameObject is active in the scene hierarchy if
[GameObject.activeSelf](GameObject-activeSelf.html) is `true` for the object
and all parent objects. A GameObject is not active in the scene hierarchy if
[GameObject.activeSelf](GameObject-activeSelf.html) is `false` for a parent
object, even if [GameObject.activeSelf](GameObject-activeSelf.html) is `true`
for the object itself.  
  
`GameObject.activeInHierarchy` changing to `false` triggers
[MonoBehaviour.OnDisable](MonoBehaviour.OnDisable.html) for attached scripts.
`GameObject.activeInHierarchy` changing to `true` triggers
[MonoBehaviour.OnEnable](MonoBehaviour.OnEnable.html).

    
    
    //This script shows how the activeInHierarchy state changes depending on the active state of the [GameObject](GameObject.html)’s parent  
      
    using UnityEngine;  
      
    public class ActiveInHierarchyExample : [MonoBehaviour](MonoBehaviour.html)
    {
        //Attach these in the Inspector
        public [GameObject](GameObject.html) m_ParentObject, m_ChildObject;
        //Use this for getting the toggle data
        bool m_Activate;  
      
        void Start()
        {
            //Deactivate parent [GameObject](GameObject.html) and toggle
            m_Activate = false;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Activate the [GameObject](GameObject.html) you attach depending on the toggle output
            m_ParentObject.SetActive(m_Activate);
        }  
      
        void OnGUI()
        {
            //[Switch](PlayerSettings.Switch.html) this toggle to activate and deactivate the parent [GameObject](GameObject.html)
            m_Activate = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(10, 10, 100, 30), m_Activate, "Activate Parent [GameObject](GameObject.html)");  
      
            if ([GUI.changed](GUI-changed.html))
            {
                //Output the status of the [GameObject](GameObject.html)'s active state in the console
                [Debug.Log](Debug.Log.html)("Child [GameObject](GameObject.html) Active : " + m_ChildObject.activeInHierarchy);
            }
        }
    }
    

Child objects of a deactivated parent GameObject may continue to be active
according to [GameObject.activeSelf](GameObject-activeSelf.html) despite being
invisible in the scene. [GameObject.activeInHierarchy](GameObject-
activeInHierarchy.html) is the reliable way to check if a GameObject has been
effectively deactivated by the status of a parent object.

    
    
    //This script shows how activeInHierarchy differs from activeSelf. Use the toggle  to alter the parent and child [GameObject](GameObject.html)’s active states. This makes it output the child [GameObject](GameObject.html)’s state in the console.
    //It also shows how activeSelf outputs that the child [GameObject](GameObject.html) is active when the parent is not, while the activeInHierarchy lists the child [GameObject](GameObject.html) as inactive.  
      
    
    using UnityEngine;  
      
    public class ActiveInHierarchyExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) m_ParentObject, m_ChildObject;
        //Use this for getting the toggle data
        bool m_ActivateParent, m_ActivateChild;
        //Use these for deciding if console is needing updated
        bool m_HierarchyOutput, m_SelfOutput;  
      
        void Start()
        {
            //Deactivate parent and child GameObjects and toggles
            m_ActivateParent = false;
            m_ActivateChild = false;
            //Ables script to output current state of [GameObject](GameObject.html) to console
            m_HierarchyOutput = false;
            m_SelfOutput = false;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Activates the [GameObject](GameObject.html) you attach depending on the toggle output
            m_ParentObject.SetActive(m_ActivateParent);
            m_ChildObject.SetActive(m_ActivateChild);  
      
            //Find out if the [GameObject](GameObject.html) is active in the Game and checks if this state has been output to the console
            if (m_HierarchyOutput == false)
            {
                //Output the state of the [GameObject](GameObject.html)’s activity if it hasn't already been output
                [Debug.Log](Debug.Log.html)("Object Active : " + m_ChildObject.activeInHierarchy);
                //The state of the [GameObject](GameObject.html) is output already, so no need to do it again
                m_HierarchyOutput = true;
            }
            //Check to see if the assigned [GameObject](GameObject.html) is active despite parent [GameObject](GameObject.html)'s status
            if (m_ChildObject.activeSelf && m_SelfOutput == false)
            {
                //Output the message if the [GameObject](GameObject.html) is still active
                [Debug.Log](Debug.Log.html)("Child Active, parent might not be");
                //You no longer need to output the message
                m_SelfOutput = true;
            }
        }  
      
        void OnGUI()
        {
            //[Switch](PlayerSettings.Switch.html) this toggle to activate and deactivate the parent [GameObject](GameObject.html)
            m_ActivateParent = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(10, 10, 100, 30), m_ActivateParent, "Activate Parent [GameObject](GameObject.html)");
            //[Switch](PlayerSettings.Switch.html) this toggle to activate and deactivate the child [GameObject](GameObject.html)
            m_ActivateChild = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(10, 40, 100, 30), m_ActivateChild, "Activate Child [GameObject](GameObject.html)");  
      
    
            //If a change is detected with the toggle, the console outputs updates
            if ([GUI.changed](GUI-changed.html))
            {
                m_SelfOutput = false;
                m_HierarchyOutput = false;
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

