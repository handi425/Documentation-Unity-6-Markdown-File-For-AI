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

**Method group is Obsolete**  

# ClusterInput

class in UnityEngine

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

**Obsolete** This type is deprecated and will be removed in Unity 7.

### Description

Interface for reading and writing inputs in a Unity Cluster.

ClusterInput provides access to VRPN devices by connecting to a VRPN server.
It also provides access to writeable inputs. All inputs managed by
ClusterInput will be replicated to the rest of the connected slaves in the
cluster. Using ClusterInput is much like using the traditional Input system in
Unity.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Buttons and [Axis](Animations.Axis.html) provide a single value.
            bool buttonValue = ClusterInput.GetButton("button1");
            float axisValue = ClusterInput.GetAxis("axis1");  
      
            // A tracker provides 2 values, rotation and position.
            [Vector3](Vector3.html) position = ClusterInput.GetTrackerPosition("tracker1");
            [Quaternion](Quaternion.html) rotation = ClusterInput.GetTrackerRotation("tracker1");  
      
            if (ClusterNetwork.isMasterOfCluster)
            {
                float axisValueCustom = MyCustomDevicePlugin.GetValue("myaxis");
                ClusterInput.SetAxis("customAxis", axisValueCustom);
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

