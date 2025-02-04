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

#  [Renderer](Renderer.html).material

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

public [Material](Material.html) material;

### Description

Returns the first instantiated [Material](Material.html) assigned to the
renderer.

Modifying `material` will change the material for this object only.  
  
If the material is used by any other renderers, this will clone the shared
material and start using it from now on.  
  
**Note:**  
This function automatically instantiates the materials and makes them unique
to this renderer. It is your responsibility to destroy the materials when the
game object is being destroyed.
[Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html) also
destroys the materials but it is usually only called when loading a new level.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Material](Material.html) m_Material;  
      
        void Start()
        {
            //Fetch the [Material](Material.html) from the [Renderer](Renderer.html) of the [GameObject](GameObject.html)
            m_Material = GetComponent<[Renderer](Renderer.html)>().material;
            print("Materials " + [Resources.FindObjectsOfTypeAll](Resources.FindObjectsOfTypeAll.html)(typeof([Material](Material.html))).[Length](UIElements.Length.html));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.A](KeyCode.A.html)))
            {
                //Output the amount of materials before [GameObject](GameObject.html) is destroyed
                print("Materials " + [Resources.FindObjectsOfTypeAll](Resources.FindObjectsOfTypeAll.html)(typeof([Material](Material.html))).[Length](UIElements.Length.html));
                //Destroy [GameObject](GameObject.html)
                Destroy(gameObject);
            }
        }  
      
        void OnMouseOver()
        {
            // Change the [Color](Color.html) of the [GameObject](GameObject.html) when the mouse hovers over it
            m_Material.color = [Color.red](Color-red.html);
        }  
      
        void OnMouseExit()
        {
            //Change the [Color](Color.html) back to white when the mouse exits the [GameObject](GameObject.html)
            m_Material.color = [Color.white](Color-white.html);
        }  
      
        void OnDestroy()
        {
            //Destroy the instance
            Destroy(m_Material);
            //Output the amount of materials to show if the instance was deleted
            print("Materials " + [Resources.FindObjectsOfTypeAll](Resources.FindObjectsOfTypeAll.html)(typeof([Material](Material.html))).[Length](UIElements.Length.html));
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

