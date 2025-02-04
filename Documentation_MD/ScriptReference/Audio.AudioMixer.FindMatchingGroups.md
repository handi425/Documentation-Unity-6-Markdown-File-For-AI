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

#  [AudioMixer](Audio.AudioMixer.html).FindMatchingGroups

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

public AudioMixerGroup[] FindMatchingGroups(string subPath);

### Parameters

subPath | Path sub-strings to match with.  
---|---  
  
### Returns

**AudioMixerGroup[]** Groups in the mixer whose paths match the specified
search path.

### Description

Connected groups in the mixer form a path from the mixer's master group to the
leaves. This path has the format **Master Group/Child of Master
Group/Grandchild of Master Group** , and so on. For example, in the hierarchy
below, the group DROPS has the path **Master/WATER/DROPS**. To return only the
group called **DROPS** , enter **DROPS**. The substring **Master/AMBIENCE**
returns three groups, **AMBIENCE/CROWD** , **AMBIENCE/ROAD** , and
**AMBIENCE**. The substring **/R** would return both **ROAD** and **RIVER**.

![](../StaticFiles/ScriptRefImages/AudioMixerFindMatchingGroupsExampleHeirarchy.png)

    
    
    using UnityEngine;
    using UnityEngine.Audio;  
      
    public class FindMatchingMixerGroups : [MonoBehaviour](MonoBehaviour.html)
    {
        public [AudioMixer](Audio.AudioMixer.html) mixer;  
      
        static void PrintGroups([AudioMixerGroup](Audio.AudioMixerGroup.html)[] groups)
        {
            [Debug.Log](Debug.Log.html)("---- MIXER GROUPS ----");
            foreach (var group in groups)
            {
                [Debug.Log](Debug.Log.html)(group);
            }
        }  
      
        void Start()
        {
            // Will find all groups with a path containing the substring "DROPS"
            // In the example, this is a single group defined by the path Master/WATER/DROPS.
            var groups = mixer.FindMatchingGroups("DROPS");
            PrintGroups(groups);  
      
            // Will find all groups with a path containing the substring "Master/AMBIENCE"
            // In the below example, this matches three groups "Master/AMBIENCE/CROWD", "Master/AMBIENCE/ROAD", and "Master/AMBIENCE".
            groups = mixer.FindMatchingGroups("Master/AMBIENCE");
            PrintGroups(groups);
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

