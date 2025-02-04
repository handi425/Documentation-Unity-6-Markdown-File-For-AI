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

#  [GameObject](GameObject.html).GetComponent

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

## Declaration

public T GetComponent();

### Returns

**T** A reference to a component of the specified type, returned as an object
of type `T`. If no component is found, returns `null`.

### Description

Retrieves a reference to a component of the specified type, by providing the
component type as a type parameter to the generic method.

`GetComponent` returns only the first matching component found on the
GameObject, and components aren't checked in a defined order. If there are
multiple components of the same type and you need to find a specific one, use
[GameObject.GetComponents](GameObject.GetComponents.html) and check the list
of components returned to identify the one you want.  
  
**Note** : If the type you request is a derivative of MonoBehaviour and the
script it's defined in can't be loaded, then this function returns `null` for
that component. This might happen if you've named your class ambiguously.
Refer to [Naming scripts](../Manual/Namespaces.html) in the Manual for more
information on naming considerations.  
  
The typical usage for this method is to call it on a reference to a different
GameObject than the one your script is on. For example:  
  
`ComponentType myComponent = otherGameObject.GetComponent<ComponentType>()`  
  
To find components attached to other GameObjects, you need a [reference to
that other GameObject](../Manual/class-
GameObject.html#AccessingOtherGameObjects), or to any component attached to
that GameObject. You can then call `GetComponent` on that reference.  
  
You can also use this method to get a reference to a component on the
GameObject that this script is attached to, by calling this method inside a
`MonoBehaviour`-derived class attached to the GameObject. You can omit the
preceding `GameObject` qualifier to reference the GameObject the script is
attached to. In this instance, you're actually calling
[Component.GetComponent](Component.GetComponent.html) because the script
itself is a type of component, but the result is the same as if you'd
referenced the GameObject itself. For example:  
  
`ComponentType myComponent = GetComponent<ComponentType>()`  
  
The following example gets a reference to a hinge joint component on the
referenced GameObject, and if found, sets a property on it.

    
    
    using UnityEngine;  
      
    public class GetComponentExample : [MonoBehaviour](MonoBehaviour.html)
    // Attach this script to a [GameObject](GameObject.html) as a component.
    {
    // Create a reference to another [GameObject](GameObject.html) in the scene. Set a value for this in the Other Game Object field
    // in the Inspector window before entering Play mode. The referenced [GameObject](GameObject.html) must contain a
    // [HingeJoint](HingeJoint.html) component.
        public [GameObject](GameObject.html) otherGameObject;  
      
        void Start()
        {
            [HingeJoint](HingeJoint.html) hinge = otherGameObject.GetComponent<[HingeJoint](HingeJoint.html)>();
            // Perform null check to confirm a valid [HingeJoint](HingeJoint.html) component was successfully returned.
            if (hinge != null)
            {
                hinge.useSpring = false;
            }
        }
    }
    

Additional resources: [Component](Component.html),
[GameObject.GetComponents](GameObject.GetComponents.html)

* * *

## Declaration

public [Component](Component.html) GetComponent(Type type);

### Parameters

type | The type of component to search for, specified as a `Type` object.  
---|---  
  
### Returns

**Component** A reference to a component of the specified type, returned as a
`Component` type. If no component is found, returns `null`.

### Description

Retrieves a reference to a component of specified type, by providing the
component type as a method parameter.

This version of `GetComponent` isn't as efficient as the generic version. Use
this version only if necessary.  
  
`GetComponent` returns only the first matching component found on the
GameObject, and components aren't checked in a defined order. If there are
multiple components of the same type and you need to find a specific one, use
[GameObject.GetComponents](GameObject.GetComponents.html) and check the list
of components returned to identify the one you want.  
  
**Note** : If the type you request is a derivative of MonoBehaviour and the
script it's defined in can't be loaded, then this function returns `null` for
that component. This might happen if you've named your class ambiguously.
Refer to [Naming scripts](../Manual/Namespaces.html) in the Manual for more
information on naming considerations.  
  
The typical usage for this method is to call it on a reference to a different
GameObject than the one your script is on. For example:  
  
`ComponentType myComponent =
otherGameObject.GetComponent(typeof(ComponentType)) as ComponentType`  
  
To find components attached to other GameObjects, you need a [reference to
that other GameObject](../Manual/class-
GameObject.html#AccessingOtherGameObjects), or to any component attached to
that GameObject. You can then call `GetComponent` on that reference.  
  
You can also use this method to get a reference to a component on the
GameObject that this script is attached to, by calling this method inside a
`MonoBehaviour`-derived class attached to the GameObject. You can omit the
preceding `GameObject` qualifier to reference the GameObject the script is
attached to. In this instance, you're actually calling
[Component.GetComponent](Component.GetComponent.html) because the script
itself is a type of component, but the result is the same as if you'd
referenced the GameObject itself. For example:  
  
`ComponentType myComponent = GetComponent(typeof(ComponentType)) as
ComponentType`  
  
The following example gets a reference to a hinge joint component on the
referenced GameObject, and if found, sets a property on it.

    
    
    using UnityEngine;  
      
    public class GetComponentExample : [MonoBehaviour](MonoBehaviour.html)
    // Attach this script to a [GameObject](GameObject.html) as a component.
    {
    // Create a reference to another [GameObject](GameObject.html) in the scene. Set a value for this in the Other Game Object field
    // in the Inspector window before entering Play mode. The referenced [GameObject](GameObject.html) must contain a
    // [HingeJoint](HingeJoint.html) component.
        public [GameObject](GameObject.html) otherGameObject;  
      
        void Start()
        {
        // This version of this method returns a [Component](Component.html), so use the as operator to safely
        // convert it to the derived [HingeJoint](HingeJoint.html) type
            [HingeJoint](HingeJoint.html) hinge = otherGameObject.GetComponent(typeof([HingeJoint](HingeJoint.html))) as [HingeJoint](HingeJoint.html);
        // Perform null check to confirm that the returned type was successfully converted to [HingeJoint](HingeJoint.html).
            if (hinge != null)
            {
                hinge.useSpring = false;
            }
        }
    }
    

Additional resources: [Component](Component.html),
[GameObject.GetComponents](GameObject.GetComponents.html)

* * *

## Declaration

public [Component](Component.html) GetComponent(string type);

### Parameters

type | The name of the type of component to search for, specified as a string.  
---|---  
  
### Returns

**Component** A reference to a component of the specified type, returned as a
`Component` type. If no component is found, returns `null`.

### Description

Retrieves a reference to a component of the specified type, by providing the
name of the component type as a method parameter.

This version of `GetComponent` isn't as efficient as the generic version. Use
this version only if necessary.  
  
`GetComponent` returns only the first matching component found on the
GameObject, and components aren't checked in a defined order. If there are
multiple components of the same type and you need to find a specific one, use
[GameObject.GetComponents](GameObject.GetComponents.html) and check the list
of components returned to identify the one you want.  
  
**Note** : If the type you request is a derivative of MonoBehaviour and the
script it's defined in can't be loaded then this function returns `null` for
that component. This might happen if you've named your class ambiguously.
Refer to [Naming scripts](../Manual/Namespaces.html) in the Manual for more
information on naming considerations.  
  
The typical usage for this method is to call it on a reference to a different
GameObject than the one your script is on. For example:  
  
`ComponentType myComponent = otherGameObject.GetComponent("ComponentType") as
ComponentType`  
  
To find components attached to other GameObjects, you need a [reference to
that other GameObject](../Manual/class-
GameObject.html#AccessingOtherGameObjects), or to any component attached to
that GameObject. You can then call `GetComponent` on that reference.  
  
You can also use this method to get a reference to a component on the
GameObject that this script is attached to, by calling this method inside a
`MonoBehaviour`-derived class attached to the GameObject. You can omit the
preceding `GameObject` qualifier to reference the GameObject the script is
attached to. In this instance, you're actually calling
[Component.GetComponent](Component.GetComponent.html) because the script
itself is a type of component, but the result is the same as if you'd
referenced the GameObject itself. For example:  
  
`ComponentType myComponent = GetComponent("ComponentType") as ComponentType`  
  
The following example gets a reference to a hinge joint component on the
referenced GameObject, and if found, sets a property on it.

    
    
    using UnityEngine;  
      
    public class GetComponentNonPerformantExample : [MonoBehaviour](MonoBehaviour.html)
    // Attach this script to a [GameObject](GameObject.html) as a component.
    {
    // Create a reference to another [GameObject](GameObject.html) in the scene. Set a value for this in the Other Game Object field
    // in the Inspector window before entering Play mode. The referenced [GameObject](GameObject.html) must contain a
    // [HingeJoint](HingeJoint.html) component.
        public [GameObject](GameObject.html) otherGameObject;  
      
        void Start()
        {
            // This version of this method returns a [Component](Component.html), so use the as operator to safely
            // convert it to the derived [HingeJoint](HingeJoint.html) type
            [HingeJoint](HingeJoint.html) hinge = otherGameObject.GetComponent("[HingeJoint](HingeJoint.html)") as [HingeJoint](HingeJoint.html);
            // Perform null check to confirm a valid [HingeJoint](HingeJoint.html) component was successfully returned.
            if (hinge != null)
            {
                hinge.useSpring = false;
            }
        }
    }
    

Additional resources: [Component](Component.html),
[GameObject.GetComponents](GameObject.GetComponents.html)

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

