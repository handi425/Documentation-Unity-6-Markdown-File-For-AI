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

#
[AssetPostprocessor](AssetPostprocessor.html).OnPostprocessGameObjectWithUserProperties(GameObject,string[],object[])

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

Gets called for each GameObject that had at least one user property attached
to it in the imported file.

The second argument string array (propNames) contains all the names of the
properties found. The System.Object array (values) contains all the actual
values. These can be of type string, Vector4, bool, Color, float, int.  
  
A typical use case for this feature is reading out "userdata" stored on
objects in 3dmax/maya. Depending on what is written in the text userdata for
an object, you could decide to postprocess your GameObject in different ways.  
  
For a detailed description of the stage when the function is invoked see
[AssetPostprocessor](AssetPostprocessor.html).  
  
Please note that the GameObjects and Meshes only exist during the import and
will be destroyed immediately afterwards. This function is called before the
final Prefab is created and before it is written to disk, thus you have full
control over the generated game objects and components. Any references to game
objects or meshes will become invalid after the import has been completed.
Thus it is not possible to create a new Prefab in a different file from
OnPostprocessGameObjectWithUserProperties that references meshes in the
imported fbx file.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;  
      
    public class ExampleClass : [AssetPostprocessor](AssetPostprocessor.html)
    {
        void OnPostprocessGameObjectWithUserProperties(
            [GameObject](GameObject.html) go,
            string[] propNames,
            System.Object[] values)
        {
            for (int i = 0; i < propNames.Length; i++)
            {
                string propName = propNames[i];
                System.Object value = (System.Object)values[i];  
      
                [Debug.Log](Debug.Log.html)("Propname: " + propName + " value: " + values[i]);  
      
                if (value.GetType().ToString() == "System.Int32")
                {
                    int myInt = (int)value;
                    // do something useful
                }  
      
                // etc...
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

